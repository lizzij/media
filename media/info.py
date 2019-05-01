# !/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

from datetime import datetime, timedelta

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from media.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint('info', __name__)

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/info', methods=['GET', 'POST'])
def get_info(user_id_hashid, day_hashid):
    """Contains information.

    To a user on a certain day
    Hash user_id and day

    :param user_hashid: hashed user_id of the user
    :param day_hashid: hashed number of day
    """

    # unhash user_id and day
    user = get_db().execute(
        'SELECT user_id, day'
        ' FROM user u'
        ' WHERE u.user_id_hashid = ? AND u.day_hashid = ?',
        (user_id_hashid, day_hashid,)
    ).fetchone()
    if user is None:
        abort(404, "User {0}/{1} doesn't exist.".format(user_id_hashid, day_hashid))
    user_id = user[0]
    day = user[1]

    # TODO change to 0
    # get day 1 hashid on day 0
    if day < 8:
        next = get_db().execute(
            'SELECT user_id_hashid, day_hashid'
            ' FROM user u'
            ' WHERE u.user_id = ? AND u.day = ?',
            (user_id, (day+1),)
        ).fetchone()
        next_user_id_hashid = next[0]
        next_day_hashid = next[1]
    else:
        next_user_id_hashid = None
        next_day_hashid = None

    last_survey_page = get_db().execute(
        'SELECT survey_page'
        ' FROM activity a'
        ' WHERE a.user_id = ? AND a.day = ?',
        (user_id, day,)
    ).fetchone()
    if last_survey_page is None:
        lastpage = 0
    elif last_survey_page[0] <= 0:
        lastpage = 0
    else:
        lastpage = last_survey_page[0]
        return redirect(url_for('info.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid))

    # direct to survey for day 7, 8
    if day > 6:
        return redirect(url_for('info.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid))

    # consent collect, redirect to day 1
    if day == 0:
        if request.method == 'POST':
            now = datetime.now()
            consent = request.form['consent']
            db = get_db()
            db.execute(
                'INSERT INTO survey (user_id, day, result, created, question_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (user_id, 0, consent, now, 'consent')
            )
            db.commit()
            if consent == 'proceed':
                return redirect(url_for('info.get_info', user_id_hashid=next_user_id_hashid, day_hashid=next_day_hashid))
            elif consent == 'notProceed':
                flash('如果您不想参与此次调研，只需关闭窗口并删除此联系人即可。如果误点“我不同意”，请点击“我同意参与”。')
        return render_template('consentForm.html', next_user_id_hashid=next_user_id_hashid, next_day_hashid=next_day_hashid)

    # retrieve info by info_id
    info = get_db().execute(
        'SELECT i.event_id,title,subtitle,info_date,info_time,location,image_file,air_quality_source,air_quality_source_logo,short_description,low_temp,high_temp,suitable_for_family,suitable_for_friends,suitable_for_lover,suitable_for_baby,suitable_for_elderly,suitable_for_pet,event_details'
        ' FROM infos i'
        ' WHERE i.event_id = ?',
        (day,)
    ).fetchone()  # TODO dynamically retrieve event id from treatment
    # TODO unlink source here
    # TODO use select * instead

    # TODO append source to info tuple and use as a variable in info.html and intoPageNoAQDetails.html
    # TODO day 6 event 1 and 2 dynamic

    # retrieve user info from user table
    # TODO merge with the first retrieve in user
    user = get_db().execute(
        'SELECT u.user_id, u.day, wechat_id, treatment, user_id_hashid, day_hashid'
        ' FROM user u'
        ' WHERE u.user_id = ? AND u.day = ?',
        (user_id, day,)
    ).fetchone()

    if info is None:
        abort(404, "Info for user_id {0} on day {1} doesn't exist.".format(user_id, day))

    # TODO dyniamically from treatment
    if day <= 3 or day == 6:
        return render_template('infoPageNoAQDetail.html', user=user, info=info)
    else:
        return render_template('infoPage.html', user=user, info=info)

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/survey', methods=['GET', 'POST'])
def get_survey(user_id_hashid, day_hashid):
    """Send survey

    According to a user's id and treatment group.
    Hash the user_id and day.
    """
    user = get_db().execute(
        'SELECT user_id, day'
        ' FROM user u'
        ' WHERE u.user_id_hashid = ? AND u.day_hashid = ?',
        (user_id_hashid, day_hashid,)
    ).fetchone()
    if user is None:
        abort(404, "User {0}/{1} doesn't exist.".format(user_id_hashid, day_hashid))
    user_id = user[0]
    day = user[1]

    if day < 8: #TODO remove next day, change to day 0
        next = get_db().execute(
            'SELECT user_id_hashid, day_hashid'
            ' FROM user u'
            ' WHERE u.user_id = ? AND u.day = ?',
            (user_id, (day+1),)
        ).fetchone()
        next_user_id_hashid = next[0]
        next_day_hashid = next[1]
    else:
        next_user_id_hashid = None
        next_day_hashid = None

    last_survey_page = get_db().execute(
        'SELECT survey_page'
        ' FROM activity a'
        ' WHERE a.user_id = ? AND a.day = ?',
        (user_id, day,)
    ).fetchone()
    if last_survey_page is None:
        lastpage = 0
    else:
        lastpage = last_survey_page[0]

    if request.method == 'POST':
        now = datetime.now()
        f = request.form
        db = get_db()

        # save answer
        for question in f.keys():
            for result in f.getlist(question):
                db.execute(
                    'INSERT INTO survey (user_id, day, result, created, question_id)'
                    ' VALUES (?, ?, ?, ?, ?)',
                    (user_id, day, result, now, question)
                )

        # update last page
        lastpage += 1
        lastpages = [5, 5, 2, 1, 1, 9, 4, 2] # second last page of survey 1-8
        day_complete = 0
        if lastpage >= lastpages[day-1]:
            lastpage = lastpages[day-1]
            day_complete = 1

        # db.execute(
        #     'UPDATE activity SET day=(?), survey_page=(?), curr_time=(?), day_complete=(?) WHERE user_id=(?)',
        #     (day, lastpage, now, day_complete, user_id)
        # )
        db.execute(
            'REPLACE INTO activity (user_id, day, survey_page, curr_time, day_complete)'
            ' VALUES (?, ?, ?, ?, ?)',
            (user_id, day, lastpage, now, day_complete)
        )
        db.commit()

    return render_template('survey' + str(day) + '.html', lastpage=lastpage, next_user_id_hashid=next_user_id_hashid, next_day_hashid=next_day_hashid)

@bp.route('/completion/detail')
def completion():
    """Show all the surveys, and all results."""
    db = get_db()
    surveys = db.execute(
        'SELECT user_id, day, question_id, result, created'
        ' FROM survey s'
        ' ORDER BY created ASC'
    ).fetchall()
    return render_template('completion.html', surveys=surveys)

@bp.route('/activity')
def activity():
    """Show all the activity"""
    db = get_db()
    activitys = db.execute(
        'SELECT user_id, day, survey_page, curr_time, day_complete'
        ' FROM activity a'
        ' ORDER BY curr_time ASC'
    ).fetchall()
    return render_template('activity.html', activitys=activitys)

## We need this at the end of info.py (also need userList.html)
@bp.route('/allUsers')
def users():
    """Show all the surveys, and all results."""
    db = get_db()
    users = db.execute(
        'SELECT user_id, day, wechat_id, treatment, user_id_hashid, day_hashid'
        ' FROM user s'
        ' ORDER BY user_id ASC'
    ).fetchall()
    return render_template('userList.html', users=users)

## We need this at the end of info.py (also need userList.html)
@bp.route('/allActivities')
def user_activities():
    """Show all the surveys, and all results."""
    db = get_db()
    users = db.execute(
        'SELECT user_id, day, day_complete, survey_page, day_started, curr_time'
        ' FROM activity s'
        ' ORDER BY user_id ASC'
    ).fetchall()
    return render_template('activityList.html', users=users)

## We need this at the end of info.py
@bp.route('/userInsert/<user_id>/<day>/<wechat_id>/<treatment>/<user_id_hashid>/<day_hashid>', methods=['POST'])
def user_insert(user_id, day, wechat_id, treatment, user_id_hashid, day_hashid):
    db = get_db()
    db.execute(
        'INSERT INTO user (user_id, day, wechat_id, treatment, user_id_hashid, day_hashid)'
        ' VALUES (?, ?, ?, ?, ?, ?)',
        (user_id, day, wechat_id, treatment, user_id_hashid, day_hashid)
    )
    db.commit()
    return 'complete'

## We need this at the end of info.py
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

## We need this at the end of info.py
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
