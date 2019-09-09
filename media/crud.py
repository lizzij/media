# !/usr/bin/env python
# encoding: utf-8
import functools
from bs4 import BeautifulSoup
import requests
from io import StringIO
import pandas as pd
import random
from math import floor
from random import randint
from hashids import Hashids

from datetime import datetime, timedelta

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from media.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint("crud", __name__)

@bp.route('/allResults')
def user_results():
    """Show all the surveys, and all results."""
    db = get_db()
    surveys = db.execute(
        'SELECT user_id, day, question_id, result, created'
        ' FROM survey s'
        ' ORDER BY created ASC'
    ).fetchall()
    return render_template('crud/surveyList.html', surveys=surveys)

@bp.route('/allUsers')
def users():
    """Show all the surveys, and all results."""
    db = get_db()
    users = db.execute(
        'SELECT user_id, day, wechat_id, treatment, cohort, user_id_hashid, day_hashid'
        ' FROM user s'
        ' ORDER BY user_id ASC'
    ).fetchall()
    return render_template('crud/userList.html', users=users)

@bp.route('/allActivities')
def user_activities():
    """Show all the surveys, and all results."""
    db = get_db()
    users = db.execute(
        'SELECT user_id, day, day_complete, survey_page, day_started, curr_time'
        ' FROM activity s'
        ' ORDER BY user_id ASC'
    ).fetchall()
    return render_template('crud/activityList.html', users=users)

@bp.route('/allEvents')
def all_events():
    """Show all the events."""
    db = get_db()
    events = db.execute(
        'SELECT * FROM infos ORDER BY info_id ASC'
    ).fetchall()
    return render_template('crud/infoList.html', events=events)

@bp.route('/eventUpdate', methods=['GET', 'POST'])
def update_events():
    info = None

    if request.method == 'POST':
        # search for event_id and cohort
        event_id = request.form['event_id']
        cohort = request.form['cohort']
        db = get_db()
        info = db.execute('SELECT * FROM infos i WHERE i.event_id = ? AND cohort = ?',(event_id, cohort,)).fetchone()
        # not in db
        if info is None:
            db.execute('INSERT INTO infos (event_id, cohort) VALUES (?, ?)',(event_id, cohort))
            info = db.execute('SELECT * FROM infos i WHERE i.event_id = ? AND cohort = ?',(event_id, cohort,)).fetchone()
            db.commit()
            flash('event_id %s and cohort %s combination not found, fill-in the rest to insert into db.' % (event_id, cohort))

        f = request.form
        db = get_db()
        for field in f.keys():
            for value in f.getlist(field):
                db.execute(
                    'UPDATE infos SET ' +field+ ' = ? WHERE event_id = ? AND cohort = ?',
                    (value, event_id, cohort))
        db.commit()
    return render_template('crud/updateEvent.html', info=info)

@bp.route('/eventDelete/<event_id>/<cohort>', methods=['GET', 'POST'])
def delete_event(event_id, cohort):
    db = get_db()
    db.execute(
        'DELETE FROM infos WHERE event_id = ? AND cohort = ?',(event_id, cohort,)
    )
    db.commit()
    return 'complete'

@bp.route('/userInsert/<user_id>/<day>/<wechat_id>/<cohort>/<treatment>/<user_id_hashid>/<day_hashid>', methods=['POST'])
def user_insert(user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid):
    db = get_db()
    db.execute(
        'INSERT INTO user (user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid)'
        ' VALUES (?, ?, ?, ?, ?, ?, ?)',
        (user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid)
    )
    db.commit()
    return 'complete'

@bp.route('/activityInsert/<user_id>', methods=['POST'])
def activity_insert(user_id):
    now = datetime.now()
    db = get_db()
    db.execute(
        'INSERT INTO activity (user_id, day, day_complete, survey_page, day_started, curr_time)'
        ' VALUES (?, ?, ?, ?, ?, ?)',
        (user_id, 1, False, 0, now, now)
    )
    db.commit()
    return 'complete'

@bp.route('/activityUpdate/<user_id>/<day>/<day_complete>/<survey_page>/<h1>/<h2>', methods=['POST'])
def activity_update(user_id,day, day_complete, survey_page, h1, h2):
    now = datetime.now()
    db = get_db()
    db.execute(
        'REPLACE INTO activity (user_id, day, day_complete, survey_page, day_started, curr_time)'
        ' VALUES (?, ?, ?, ?, ?, ?)',
        (user_id, day, day_complete, survey_page, now - timedelta(hours = int(h1)), now - timedelta(hours = int(h2)))
    )
    db.commit()
    return 'complete'

@bp.route('/getLink', methods=['GET', 'POST'])
def get_link_for_surveyor():
    if request.method == 'POST':
        surveyorNumber = request.form['surveyorNumber']
        return redirect(url_for('crud.get_link', surveyorNumber=surveyorNumber))
    return render_template('crud/surveyorNumber.html')

# to get links for a surveyor with corresponding surveyour number
@bp.route('/<string:surveyorNumber>/getLink', methods=['GET', 'POST'])
def get_link(surveyorNumber):
    URL = "https://dailyeventinfo.com/"
    msg_ineligible = u'<br><b>请发送以下消息给该好友</b>：<br><br>很抱歉，由于您已参与过我们之前的调研，您将无法参与此次调研。感谢您的积极参与。'
    msg_maxnum_cohort = u'<br><b>请发送以下消息给该好友</b>：<br><br>本轮招募已完成，我们将在下轮开始时尽快联系您！'
    msg_initial = u'<br><b>请发送以下消息给该好友</b>：<br><br><b>🔻copy below</b><br><br>我们将在接下来的6天（包括今天）每天提供一些上海本地及周边的户外活动及场所的信息。我们将向您询问一些简短的问题（约5分钟)。<br><br>\
    我们也将会询问您一些关于各类话题的问题。 如果您想参加这项学术调研，请点击以下链接开始。 您的回答仅被用于学术研究，我们将对您的个人信息及回答进行严格保密。 调研结束后我们将进行抽奖，所有参与并完成调研的同学将有机会赢得800元人民币作为奖励。<br><br>\
    如果您遇到了技术上的问题（列入网页无法正常显示等），请您在此发微信告诉我们，我们将尽快解决。<br><br>'

    ## Parameters
    cohort = "4"
    maxnum_cohort = 70 ## Maximum number of cohorts in this trial per surveyor
    maxday = 8
    seq = [3, 2, 1, 1, 3, 1, 0, 1, 0, 3, 2, 2, 1, 1, 3, 3, 2, 1, 3, 3, 3, 3, 2, 3, 2, 0, 0, 2, 2, 0, 1, 0, 1, 1, 1, 0, 0, 0, 2, 1, 1, 0, 3, 3, 2, 3, 0, 0, 2, 0, 2, 3, 1, 2, 2, 0, 2, 1, 3, 2, 0, 1, 3, 3, 0, 1, 1, 0, 1, 3, 1, 2, 2, 2, 3, 0, 3, 0, 2, 0, 2, 2, 2, 1, 1, 2, 3, 3, 1, 3, 3, 0, 2, 3, 1, 1, 0, 1, 2, 1, 1, 2, 0, 3, 3, 2, 0, 2, 0, 0, 2, 0, 1, 3, 2, 1, 0, 2, 0, 1, 1, 1, 2, 3, 0, 0, 1, 1, 0, 3, 0, 2, 2, 3, 3, 3, 3, 0, 2, 3, 3, 1, 3, 2, 1, 1, 3, 0, 0, 3, 1, 2, 1, 2, 3, 3, 1, 3, 3, 2, 3, 0, 1, 0, 2, 3, 3, 0, 1, 0, 2, 3, 1, 2, 3, 0, 3, 0, 0, 2, 2, 3, 3, 2, 0, 1, 0, 1, 1, 0, 2, 2, 2, 2, 1, 1, 1, 0, 1, 1, 3, 2, 2, 0, 1, 0, 1, 2, 3, 0, 0, 0, 1]
    # Note: the sequence is created randomly from "treatSequence.py"

    ## Get list of users
    def get_users():
        db = get_db()
        users = pd.read_sql_query('SELECT user_id, day, wechat_id, treatment, cohort, user_id_hashid, day_hashid FROM user s ORDER BY user_id ASC', db)
        return users

    ## Using the input, create user profile in DB, and produce output
    def new_user_process(input_ID):
        db = get_db()
        users = get_users()
        cohort_users = users.loc[users.cohort == int(cohort)].drop_duplicates(subset=['user_id'])
        if len(cohort_users) != 0: cohort_users['surveyor'] = int((max(pd.to_numeric(cohort_users['user_id'])) / 1e6) % 10)
        curr_cohort_user_count = int(len(set(cohort_users.loc[cohort_users.surveyor==surveyorNumber]['user_id'])))
        if input_ID in list(set(users.loc[users.cohort != int(cohort)]['wechat_id'])): # Already existing user from prev. cohorts
            return [u'<b><font color="red">该用户已存在</font></b>！',msg_ineligible]

        elif input_ID in list(set(cohort_users['wechat_id'])): # Already existing user in current cohort
            if (int(cohort_users.loc[cohort_users.wechat_id == input_ID].iloc[0]['surveyor']) != int(surveyorNumber)):
                return [u'<font color="red">（其他研究员已输入过该微信号！请不要发送任何信息，并将此用户告知 Zixin 子鑫）<br></font>']
            else:
                theUser = cohort_users.loc[(cohort_users.wechat_id == input_ID) & (cohort_users.day == 0)]
                msg_URL = URL+"shanghai/"+theUser.user_id_hashid.iloc[0]+"/"+theUser.day_hashid.iloc[0]+"/info"
                return [u'<b><font color="red">（您已输入过该微信号！）<br></font>请将其备注名改为</b>：\
                <span style="background-color:PaleGreen;">'+str(theUser.user_id.iloc[0]),msg_initial+msg_URL+'<br><br><b>🔺copy above (do not forget URL)</b><span>']

        elif curr_cohort_user_count >= maxnum_cohort: # Max cohort size reached
            db.execute(
                'INSERT INTO user (user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?)',
                ('WAITLIST', 'TBD', str(input_ID), str(int(cohort)+1), 'TBD', 'TBD', 'TBD')
            )
            db.commit()
            return ["MAX SIZE REACHED: SAVED IN WAITLIST",msg_maxnum_cohort]
        else:
            # Create nickname #
            if len(cohort_users) == 0: previousMax = 0
            else: previousMax = int((max(pd.to_numeric(cohort_users['user_id'])) % 1e6) / 1e3)
            nextUserID = int(int(cohort)*1e7 + int(surveyorNumber)*1e6 + (previousMax+1)*1e3 + randint(1,999))
            # Assign treatment group #
            treatment = "T"+str(seq[previousMax]+1)
            # Save user profile in allUsers #
            for day in range(maxday+1):
                user_id_hashids = Hashids(salt=str(10 * nextUserID + day) + "user_id", min_length=16)
                day_hashids = Hashids(salt=str(10 * nextUserID + day) + "day", min_length=10)
                hashed_user_id = user_id_hashids.encrypt(nextUserID)
                hashed_day = day_hashids.encrypt(day)
                db.execute(
                    'INSERT INTO user (user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid)'
                    ' VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (str(nextUserID), str(day), str(input_ID), str(cohort), str(treatment), hashed_user_id, hashed_day)
                )
                db.commit()
                if day == 0: msg_URL = URL+"shanghai/"+hashed_user_id+"/"+hashed_day + "/info"
            # Set up initial allActivities #
            now = datetime.now()
            db.execute(
                'REPLACE INTO activity (user_id, day, day_complete, survey_page, day_started, curr_time)'
                ' VALUES (?, ?, ?, ?, ?, ?)',
                (str(nextUserID), 0, 0, 0, now, now)
            )
            db.commit()
            # Return output for surveyors #
            return [u'<b>请将其备注名改为</b>：'+'<span style="background-color:PaleGreen;">'+str(nextUserID),msg_initial+msg_URL+'<br><br><b>🔺copy above (do not forget URL)</b><span>']

    input_ID = '/'
    output = [u'<font color="gray">（还未输入，请在上方框内输入新好友的微信号...）</font>']
    if request.method == 'POST':
        input_ID = request.form['wechatID']
        cohort = '4'
        output = new_user_process(input_ID)

    # TODO add forwarding email instructions
    surveyor = ''
    surveyorNumberDict = {'1':u'牛子琦', '2':u'王岚', '3':u'赵奕菲'}
    surveyor = surveyorNumberDict[surveyorNumber]
    return render_template('crud/getLink.html', surveyor=surveyor, input_ID=input_ID, output=output)

# to update (backlog) wechat_id for corresponding user_id
@bp.route('/updateWechatID', methods=['GET', 'POST'])
def update_wechatID():
    db = get_db()
    output_message = ''
    if request.method == 'POST':
        user_id = request.form['user_id']
        wechat_id = request.form['wechat_id']
        cohort = request.form['cohort']
        user = db.execute(
            'SELECT user_id, day, treatment, cohort'
            ' FROM user u'
            ' WHERE u.user_id = ? AND u.cohort = ?',
            (user_id, cohort,)
        ).fetchone()
        if user is None:
            db.execute(
                'INSERT INTO user (user_id, day, wechat_id, cohort, treatment, user_id_hashid, day_hashid)'
                ' VALUES (?, ?, ?, ?, ?, ?, ?)',
                (user_id, 99, wechat_id, cohort, 'treatment', 'user_id_hashid', 'day_hashid')
            )
            db.commit()
            output_message = 'Done:) <b>Inserted</b> user with user_id %s, wechat_id %s, cohort %s' % (user_id, wechat_id, cohort)
        else:
            db.execute(
                'UPDATE user SET wechat_id=?, cohort = ? WHERE user_id = ?',
                (wechat_id, cohort, user_id)
            )
            db.commit()
            output_message = 'Done:) <b>Updated</b> user with user_id %s, wechat_id %s, cohort %s' % (user_id, wechat_id, cohort)
    return render_template('crud/updateWechatID.html', output_message=output_message)
