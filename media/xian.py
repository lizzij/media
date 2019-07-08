# !/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

from datetime import datetime, timedelta

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from media.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint("xian", __name__, url_prefix="/xian")

def get_user(user_id_hashid, day_hashid, cohort = 3):
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

def get_event_info(event_id, cohort = 1): # TODO TODO TODO TODO TODO TODO: change 1 to 3 TODO TODO TODO TODO TODO TODO
    info = get_db().execute(
        'SELECT i.event_id,title,subtitle,info_date,info_time,location,image_file,short_description,low_temp,high_temp,suitable_for_family,suitable_for_friends,suitable_for_lover,suitable_for_baby,suitable_for_elderly,suitable_for_pet,event_details,phrase_for_week, phrase_for_day, phrase_for_header'
        ' FROM infos i'
        ' WHERE i.event_id = ? AND cohort = ?',
        (event_id, cohort,)
    ).fetchone()
    return info

def get_lastpage(user_id, day):
    db = get_db()
    lastpage = db.execute(
        'SELECT survey_page, day'
        ' FROM activity a'
        ' WHERE a.user_id = ?',
        (user_id,)
    ).fetchone()
    if lastpage is None:
        # TODO TODO TODO TODO TODO TODO comment out if using chatbot to post update activity TODO TODO TODO TODO TODO TODO
        now = datetime.now()
        db = get_db()
        db.execute(
            'INSERT INTO activity (user_id, day, day_complete, survey_page, day_started, curr_time)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (user_id, day, False, 0, now, now)
        )
        db.commit()
        # TODO TODO TODO TODO TODO TODO comment out if using chatbot to post update activity TODO TODO TODO TODO TODO TODO
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

    day_to_template_dict = {1:'', 2:'AQ'}
    template = day_to_template_dict[day]

    day_to_info_id_dict = {1:1, 2:2} # TODO TODO TODO TODO TODO TODO change event_id to 1:10, 2:info_id (for day 2) TODO TODO TODO TODO TODO TODO
    info = get_event_info(day_to_info_id_dict[day])

    air_quality_source = u'西安市生态环境局'
    air_quality_source_logo = u'img/SourceXaepbLogo.jpeg'

    # if competed direct to last saved survey page (skip info)
    lastpage = get_lastpage(user_id, day)
    if lastpage > 0: # have seen the survey page
        return redirect(url_for('xian.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid))

    return render_template('xian/infoPage' + template + '.html', info=info, user_id_hashid=user_id_hashid, day_hashid=day_hashid, air_quality_source=air_quality_source, air_quality_source_logo=air_quality_source_logo)

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/survey', methods=['GET', 'POST'])
def get_survey(user_id_hashid, day_hashid):
    user = get_user(user_id_hashid, day_hashid)
    user_id = user[0]
    day = user[1]
    treatment = user[2]

    # mark info page as read
    lastpage = get_lastpage(user_id, day)
    if lastpage == 0: # if reading for the first time
        update_lastpage(1, 0, user_id, day)

    # mark as completed
    day_to_lastpage_dict = {1:10, 2:10} # number of pages counting from 1 (different implementation from pilot)
    if lastpage == day_to_lastpage_dict[day]:
        update_lastpage(lastpage, 1, user_id, day)

    walkathon = {'phrase_for_day':u'2019年7月27日', 'phrase_for_week':u'2019年7月22-28日'}

    return render_template('xian/survey' + str(day) + '.html', walkathon=walkathon)
