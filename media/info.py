# !/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from media.db import get_db
from werkzeug.exceptions import abort

bp = Blueprint('info', __name__)
now = datetime.now()

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/info', methods=['GET', 'POST'])
def get_info(user_id_hashid, day_hashid):
    """Contains information.

    To a user on a certain day
    Hash user_id and day

    :param user_hashid: hashed user_id of the user
    :param day_hashid: hashed number of day
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

    next = get_db().execute(
        'SELECT user_id_hashid, day_hashid'
        ' FROM user u'
        ' WHERE u.user_id = ? AND u.day = ?',
        ((user_id+1), 1,)
    ).fetchone()
    next_user_id_hashid = next[0]
    next_day_hashid = next[1]

    if day == 0:
        if request.method == 'POST':
            consent = request.form['consent']
            error = None

            if not consent:
                error = '请选择.'

            if error is not None:
                abort(404, "Consent error")
            else:
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

    info = get_db().execute(
        'SELECT i.event_id,title,subtitle,info_date,info_time,location,image_file,air_quality_source,air_quality_source_logo,headword,short_description,low_temp,high_temp,suitable_for_family,suitable_for_friends,suitable_for_lover,suitable_for_baby,suitable_for_elderly,suitable_for_pet,event_details'
        ' FROM infos i'
        ' WHERE i.event_id = ?',
        (day,)
    ).fetchone()

    user = get_db().execute(
        'SELECT u.user_id, u.day, wechat_id, treatment, user_id_hashid, day_hashid'
        ' FROM user u'
        ' WHERE u.user_id = ? AND u.day = ?',
        (user_id, day,)
    ).fetchone()

    if info is None:
        abort(404, "Info for user_id {0} on day {1} doesn't exist.".format(user_id, day))

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

    if request.method == 'POST':
        f = request.form
        for question in f.keys():
            for result in f.getlist(question):
                db = get_db()
                db.execute(
                    'INSERT INTO survey (user_id, day, result, created, question_id)'
                    ' VALUES (?, ?, ?, ?, ?)',
                    (user_id, day, result, now, question)
                )
                db.commit()

    return render_template('survey' + str(day) + '.html')

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
