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

def get_user(user_id_hashid, day_hashid, cohort = 5):
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

def get_event_info(event_id, cohort = 5):
    info = get_db().execute(
        'SELECT i.event_id,title,subtitle,info_date,info_time,location,image_file,short_description,low_temp,high_temp,suitable_for_family,suitable_for_friends,suitable_for_lover,suitable_for_baby,suitable_for_elderly,suitable_for_pet,event_details,phrase_for_week, phrase_for_day, phrase_for_header'
        ' FROM infos i'
        ' WHERE i.event_id = ? AND cohort = ?',
        (event_id, cohort,)
    ).fetchone()
    return info

def get_lastpage(user_id, day, day_to_lastpage_dict = {1:6, 2:5, 3:3, 4:1, 5:1, 6:13, 7:5, 8:3}): # excluding the info & final page
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

def get_last_question(user_id):
    db = get_db()
    last_question_query = db.execute(
        'SELECT question_id'
        ' FROM survey s'
        ' WHERE s.user_id = ?'
        ' ORDER BY s.created DESC LIMIT 1',
        (user_id,)
    ).fetchone()
    if last_question_query:
        last_question = last_question_query[0]
    else:
        last_question = 'null'
    return last_question

def get_page_from_question_name(day, question_name, cohort = 5):
    db = get_db()
    page_query = db.execute(
        'SELECT page'
        ' FROM pages p'
        ' WHERE p.day = ? AND p.cohort = ? AND p.question_name = ?',
        (day, cohort, question_name,)
    ).fetchone()
    if page_query:
        page = page_query[0]
    else:
        page = 0
    return page

def update_lastpage(lastpage, day_complete, user_id, day):
    now = datetime.now()
    db = get_db()
    db.execute(
        'UPDATE activity SET survey_page = ?, curr_time = ?, day_complete = ? WHERE user_id = ? AND day = ?',
        (lastpage, now, day_complete, user_id, day,)
    )
    db.commit()

def get_activity_day(user_id):
    db = get_db()
    activity_day = db.execute(
        'SELECT user_id, day'
        ' FROM activity a'
        ' WHERE a.user_id = ?',
        (user_id,)
    ).fetchone()
    day = activity_day[1]
    return day

def get_survey_answer(user_id, day):
    db = get_db()
    answers = db.execute(
        'SELECT question_id, result'
        ' FROM survey s'
        ' WHERE s.user_id = ? AND s.day = ?',
        (user_id, day, )
    ).fetchall()
    if answers:
        return answers
    return None

def check_result(user_id, day):
    correct_answer_dict = {
        2: { 'eventName': 'name1', 'eventNameOrder': None },
    }
    answers = get_survey_answer(user_id, day)
    all_correct = True
    for answer in answers:
        question = answer['question_id']
        result = answer['result']
        correct_answer = correct_answer_dict[day][question] or result
        all_correct = all_correct and (result == correct_answer)
    return all_correct

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/info', methods=['GET', 'POST'])
def get_info(user_id_hashid, day_hashid):
    user = get_user(user_id_hashid, day_hashid)
    user_id = user[0]
    day = user[1]
    treatment = user[2]
    user = {'treatment':treatment, 'day':day, 'user_id_hashid':user_id_hashid, 'day_hashid':day_hashid}

    # show survey not available on day 99
    if get_activity_day(user_id) == 99:
        return u'抱歉，此调查已过时效。'

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
        if get_activity_day(user_id) > 0:
            return redirect(url_for('shanghai.get_info', user_id_hashid=day1_user_id_hashid, day_hashid=day1_day_hashid))
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

    # get event details if on day 1-6 (cohort set to 5)
    day_to_info_id_dict = {1:20, 2:21, 3:22, 4:23, 5:24, 6:25}
    info = get_event_info(day_to_info_id_dict[day])

    # air quality source for treatment groups different on day 6
    treatment_to_aq_source_dict = {'T0':'', 'T1':'', 'T2-1':u'（来自：上海市环境监测中心）', 'T2-2':u'（来自：上海广播电视台-STV新闻坊）', 'T3':u'（来自：新闻晨报）'}
    treatment_to_aq_source_logo_dict = {'T0':'img/transparent.png', 'T1':'img/transparent.png', 'T2-1':'img/SourceSHEnvironmentLogo.jpg', 'T2-2':'img/SourceSTVLogo.png', 'T3':'img/SourceMorningPostLogo.jpg'}
    air_quality_source = treatment_to_aq_source_dict[treatment]
    air_quality_source_logo = treatment_to_aq_source_logo_dict[treatment]
    air_quality = {'air_quality_source':air_quality_source, 'air_quality_source_logo':air_quality_source_logo}

    # if competed direct to last saved survey page (skip info)
    lastpage = get_lastpage(user_id, day)
    if lastpage > 0: # have seen the survey page
        return redirect(url_for('shanghai.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid))

    return render_template('shanghai/infoPage' + template + '.html', info=info, user=user, air_quality=air_quality)

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/survey', methods=['GET', 'POST'])
def get_survey(user_id_hashid, day_hashid, optional_last_page=None):
    user = get_user(user_id_hashid, day_hashid)
    user_id = user[0]
    day = user[1]
    treatment = user[2]
    user = {'treatment':treatment, 'user_id_hashid':user_id_hashid, 'day_hashid':day_hashid}

    second_event = get_event_info(26,5)
    walkathon = get_event_info(20,5)

    t0_air_quality_source = { 'second_event' : { 'air_quality_source':u'', 'air_quality_source_logo':'img/transparent.png' },
                              'walkathon' : { 'air_quality_source':u'', 'air_quality_source_logo':'img/transparent.png' } }
    t1_air_quality_source = { 'second_event' : { 'air_quality_source':u'', 'air_quality_source_logo':'img/transparent.png' },
                              'walkathon' : { 'air_quality_source':u'（来自：上海市环境监测中心）', 'air_quality_source_logo':'img/SourceSHEnvironmentLogo.jpg' } }
    t2_1_air_quality_source = { 'second_event' : { 'air_quality_source':u'（来自：上海市环境监测中心）', 'air_quality_source_logo':'img/SourceSHEnvironmentLogo.jpg' },
                              'walkathon' : { 'air_quality_source':u'（来自：上海市环境监测中心）', 'air_quality_source_logo':'img/SourceSHEnvironmentLogo.jpg' } }
    t2_2_air_quality_source = { 'second_event' : { 'air_quality_source':u'（来自：上海广播电视台-STV新闻坊）', 'air_quality_source_logo':'img/SourceSTVLogo.png' },
                            'walkathon' : { 'air_quality_source':u'（来自：上海市环境监测中心）', 'air_quality_source_logo':'img/SourceSHEnvironmentLogo.jpg' } }
    t3_air_quality_source = { 'second_event' : { 'air_quality_source':u'（来自：新闻广播FM93.4）', 'air_quality_source_logo':'img/SourceNewsRadioLogo.jpg' },
                              'walkathon' : { 'air_quality_source':u'（来自：上海市环境监测中心）', 'air_quality_source_logo':'img/SourceSHEnvironmentLogo.jpg' } }
    treatment_to_air_quality_dict = {'T0': t0_air_quality_source, 'T1': t1_air_quality_source, 'T2-1': t2_1_air_quality_source, 'T2-2': t2_2_air_quality_source, 'T3': t3_air_quality_source}
    air_quality = treatment_to_air_quality_dict[treatment]


    # show survey not available on day 99
    if get_activity_day(user_id) == 99:
        return u'抱歉，此调查已过时效。'

    # mark info page as read
    last_question = get_last_question(user_id)
    lastpage = get_page_from_question_name(day, last_question)
    # update last page, activity (for day completion)
    current_page = lastpage + 1
    update_lastpage(current_page, 0, user_id, day)

    day_to_lastpage_dict = {1:6, 2:5, 3:3, 4:1, 5:1, 6:13, 7:5, 8:3}
    if current_page == day_to_lastpage_dict[day]:
        update_lastpage(current_page, 1, user_id, day)
    # mark as completed

    # go to next page on valid submit
    if optional_last_page:
        lastpage = optional_last_page

    if request.method == 'POST':
        form = request.form
        now = datetime.now()
        db = get_db()

        # save answer
        for question in form.keys():
            for result in form.getlist(question):
                db.execute(
                    'INSERT INTO survey (user_id, day, result, created, question_id)'
                    ' VALUES (?, ?, ?, ?, ?)',
                    (user_id, day, result, now, question)
                )
                db.commit()

        # check answer and redirect if needed
        if day in [2, 3, 4, 5, 6] and current_page == 1:
            if_all_correct = check_result(user_id, day)
        return redirect(url_for('shanghai.get_survey', user_id_hashid=user_id_hashid, day_hashid=day_hashid, optional_last_page=current_page))

    return render_template('shanghai/survey' + str(day) + '.html', user=user, lastpage=lastpage, second_event=second_event, walkathon=walkathon, air_quality=air_quality)
