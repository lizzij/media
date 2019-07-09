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

def get_lastpage(user_id, day, day_to_lastpage_dict = {1:4, 2:9}):
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
    user = {'treatment':treatment, 'user_id_hashid':user_id_hashid, 'day_hashid':day_hashid}

    # Air quality info to be shown only to Groups TRO/TRN, not to TNO/TNN
    treatment_day_to_template_dict = { 'TNO' : {1:'', 2:''}, 'TNN' : {1:'', 2:''}, 'TRO' : {1:'', 2:'AQ'}, 'TRN' : {1:'', 2:'AQ'}}
    template = treatment_day_to_template_dict[treatment][day]

    day_to_info_id_dict = {1:1, 2:2} # TODO TODO TODO TODO TODO TODO change event_id to 1:10, 2:info_id (for day 2) TODO TODO TODO TODO TODO TODO
    info = get_event_info(day_to_info_id_dict[day])

    day_to_air_quality_source_dict = {1:u'', 2:u'华商报'}
    day_to_air_quality_source_logo_dict = {1:'img/transparent.png', 2:'img/SourceHSBLogo.png'}
    air_quality_source = day_to_air_quality_source_dict[day]
    air_quality_source_logo = day_to_air_quality_source_logo_dict[day]
    air_quality = {'air_quality_source':air_quality_source, 'air_quality_source_logo':air_quality_source_logo}

    # if competed direct to last saved survey page (skip info)
    lastpage = get_lastpage(user_id, day)
    if lastpage > 0: # have seen the survey page
        return redirect(url_for('xian.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid))

    return render_template('xian/infoPage' + template + '.html', info=info, user=user, air_quality=air_quality)

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/survey', methods=['GET', 'POST'])
def get_survey(user_id_hashid, day_hashid):
    user = get_user(user_id_hashid, day_hashid)
    user_id = user[0]
    day = user[1]
    treatment = user[2]

    # mark info page as read
    lastpage = get_lastpage(user_id, day)
    # mark as completed
    day_to_lastpage_dict = {1:4, 2:9}

    if request.method == 'POST':
        form = request.form
        now = datetime.now()
        db = get_db()

        # default do not go to next page on refresh or submit
        global to_next_page
        to_next_page = False

        # save answer
        for question in form.keys():
            for result in form.getlist(question):
                # check if answer already exists (prevent duplication)
                previous_result = db.execute(
                    'SELECT result'
                    ' FROM survey s'
                    ' WHERE s.user_id = ? AND s.day = ? AND s.question_id = ?',
                    (user_id, day, question)
                ).fetchone()

                # save result if not duplicated
                if previous_result is None:
                    # and go to next page
                    to_next_page = True
                    db.execute(
                        'INSERT INTO survey (user_id, day, result, created, question_id)'
                        ' VALUES (?, ?, ?, ?, ?)',
                        (user_id, day, result, now, question)
                    )
                    db.commit()

        # update last page, activity (for day completion)
        if to_next_page:
            lastpage += 1
            update_lastpage(lastpage, 0, user_id, day)
            if lastpage == day_to_lastpage_dict[day]:
                update_lastpage(lastpage, 1, user_id, day)

    second_event = get_event_info(7,2) # TODO TODO TODO TODO TODO TODO change event id later TODO TODO TODO TODO TODO TODO
    walkathon = get_event_info(8,2) # TODO TODO TODO TODO TODO TODO change to 10,3 TODO TODO TODO TODO TODO TODO

    return render_template('xian/survey' + str(day) + '.html', lastpage=lastpage, second_event=second_event, walkathon=walkathon)
