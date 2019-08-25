# !/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

from datetime import datetime, timedelta

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from media.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint("shanghai", __name__, url_prefix="/shanghai")

def get_user(user_id_hashid, day_hashid, cohort = 4):
    user = get_db().execute(
        'SELECT user_id, day, treatment'
        ' FROM user u'
        ' WHERE u.user_id_hashid = ? AND u.day_hashid = ? AND u.cohort = ?',
        (user_id_hashid, day_hashid, cohort,)
    ).fetchone()
    if user is None:
        abort(404, "User {0}/{1}/{2} doesn't exist.".format(user_id_hashid, day_hashid, cohort))
    else:
        return user

def get_event_info(event_id, cohort = 4):
    info = get_db().execute(
        'SELECT i.event_id,title,subtitle,info_date,info_time,location,image_file,short_description,low_temp,high_temp,suitable_for_family,suitable_for_friends,suitable_for_lover,suitable_for_baby,suitable_for_elderly,suitable_for_pet,event_details,phrase_for_week, phrase_for_day, phrase_for_header'
        ' FROM infos i'
        ' WHERE i.event_id = ? AND cohort = ?',
        (event_id, cohort,)
    ).fetchone()
    return info

def get_lastpage(user_id, day, day_to_lastpage_dict = {1:6, 2:6, 3:3, 4:0, 5:1, 6:12, 7:5, 8:3}): # excluding the info & final page
    db = get_db()
    last_activity = db.execute(
        'SELECT survey_page, day'
        ' FROM activity a'
        ' WHERE a.user_id = ?',
        (user_id,)
    ).fetchone()
    if last_activity is None:
        lastpage = 0
    else:
        lastday = last_activity[1]
        if day < lastday: # completed
            lastpage = day_to_lastpage_dict[day]
        elif day == lastday: # partially completed
            lastpage = last_activity[0]
        else:
            lastpage = 0
    return lastpage

def update_lastpage(lastpage, day_complete, user_id, day):
    now = datetime.now()
    db = get_db()
    db.execute(
        'UPDATE activity SET survey_page = ?, curr_time = ?, day_complete = ? WHERE user_id = ? AND day = ?',
        (lastpage, now, day_complete, user_id, day,)
    )
    db.commit()

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/info', methods=['GET', 'POST'])
def get_info(user_id_hashid, day_hashid):
    user = get_user(user_id_hashid, day_hashid)
    user_id = user[0]
    day = user[1]
    treatment = user[2]
    user = {'treatment':treatment, 'day':day, 'user_id_hashid':user_id_hashid, 'day_hashid':day_hashid}

    # consent form on day 0
    if day == 0:
        db = get_db()
        day1 = db.execute(
            'SELECT user_id_hashid, day_hashid'
            ' FROM user u'
            ' WHERE u.user_id = ? AND u.day = ?',
            (user_id, 1,)
        ).fetchone()
        day1_user_id_hashid = day1[0]
        day1_day_hashid = day1[1]
        if request.method == 'POST':
            now = datetime.now()
            consent = request.form['consent']
            db.execute(
                'INSERT INTO survey (user_id, day, result, created, question_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (user_id, 0, consent, now, 'consent')
            )
            db.commit()
            # redirect to day 1 info page if consented
            if consent == 'proceed':
                db.execute(
                    'UPDATE activity SET day=?, day_complete = ?, curr_time = ? WHERE user_id = ?',
                    (1, 0, now, user_id)
                )
                db.commit()
                return redirect(url_for('shanghai.get_info', user_id_hashid=day1_user_id_hashid, day_hashid=day1_day_hashid))
            # show alert box if not to proceed
            elif consent == 'notProceed':
                flash(u'如果您不想参与此次调研，只需关闭窗口并删除此联系人即可。如果误点“我不同意”，请点击“我同意参与”。')
        return render_template('shanghai/consentForm.html')

    # only show AQ to T2/3/4 on day 6
    if day == 6 and treatment != 'T1':
        template = 'AQ'
    else:
        template = ''

    # direct to survey for day 7, 8 (no info)
    if day > 6:
        return redirect(url_for('shanghai.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid))

    # get event details if on day 1-6 (cohort set to 4)
    day_to_info_id_dict = {1:13, 2:14, 3:15, 4:16, 5:17, 6:18}
    info = get_event_info(day_to_info_id_dict[day])

    # air quality source for treatment groups different on day 6
    treatment_to_aq_source_dict = {'T1':'', 'T2':u'（来自：上海市环境监测中心）', 'T3':u'（来自：新闻晨报）', 'T4':u'（来自：[TBD]）' }
    treatment_to_aq_source_logo_dict = {'T1':'img/transparent.png', 'T2':'img/SourceSHEnvironmentLogo.jpg', 'T3':'img/SourceMorningPostLogo.jpg', 'T4':'img/SourceTBD.png' }
    air_quality_source = treatment_to_aq_source_dict[treatment]
    air_quality_source_logo = treatment_to_aq_source_logo_dict[treatment]
    air_quality = {'air_quality_source':air_quality_source, 'air_quality_source_logo':air_quality_source_logo}

    # if competed direct to last saved survey page (skip info)
    lastpage = get_lastpage(user_id, day)
    if lastpage > 0: # have seen the survey page
        return redirect(url_for('shanghai.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid))

    return render_template('shanghai/infoPage' + template + '.html', info=info, user=user, air_quality=air_quality)

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/survey', methods=['GET', 'POST'])
def get_survey(user_id_hashid, day_hashid):
    # return render_template('crud/home.html')
    return "Hello {0} {1}!!".format(user_id_hashid, day_hashid)
