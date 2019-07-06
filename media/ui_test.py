# !/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

from datetime import datetime, timedelta

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from media.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint('ui_test', __name__)

@bp.route('/test/<string:hashed_user_id>/<string:hashed_treatment>/info')
def info_test(hashed_user_id, hashed_treatment):
    user_id = '10' + hashed_user_id[12] + hashed_user_id[3]
    treatment = hashed_treatment[7]

    # check if user already read the info page
    read = get_db().execute(
        'SELECT result'
        ' FROM survey s'
        ' WHERE s.user_id = ? AND s.day = ? AND s.question_id = ?',
        (user_id, 10, "readInfo")
    ).fetchone()

    # not read yet
    if read is None:

        # get test info and sources
        info = get_db().execute(
            'SELECT i.event_id,title,subtitle,info_date,info_time,location,image_file,short_description,low_temp,high_temp,suitable_for_family,suitable_for_friends,suitable_for_lover,suitable_for_baby,suitable_for_elderly,suitable_for_pet,event_details,phrase_for_week, phrase_for_day, phrase_for_header'
            ' FROM infos i'
            ' WHERE i.event_id = ? AND cohort = ?',
            (9, 1,)
        ).fetchone()
        curr_air_quality_source = u'（来自：北京晚报）'
        curr_air_quality_source_logo = 'img/SourceBJEN.png'
        return render_template('ui_test/infoPage' + treatment + '.html', hashed_user_id=hashed_user_id, hashed_treatment=hashed_treatment, info=info, air_quality_source=curr_air_quality_source, air_quality_source_logo=curr_air_quality_source_logo)

    # read info already, skip to survey
    else:
        return redirect(url_for('ui_test.info_test_survey', hashed_user_id=hashed_user_id, hashed_treatment=hashed_treatment))

@bp.route('/test/<string:hashed_user_id>/<string:hashed_treatment>/survey', methods=['GET', 'POST'])
def info_test_survey(hashed_user_id, hashed_treatment):
    user_id = '10' + hashed_user_id[12] + hashed_user_id[3]
    treatment = hashed_treatment[7]

    # record info page as read by user
    db = get_db()
    now = datetime.now()
    db.execute(
        'INSERT INTO survey (user_id, day, result, created, question_id)'
        ' VALUES (?, ?, ?, ?, ?)',
        (user_id, 10, "read", now, "readInfo")
    )
    db.commit()

    if request.method == 'POST':
        questions = ['eventName', 'eventNameOrder', 'airQuality', 'source', 'sourceOrder']
        now = datetime.now()
        db = get_db()
        for question in questions:
            answer = request.form[question]
            db.execute(
                'INSERT INTO survey (user_id, day, result, created, question_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (user_id, 10, answer, now, question)
            )
        db.commit()
        return render_template('pilot/completionPage.html')
    return render_template('pilot/surveyInfo.html')
