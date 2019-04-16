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
    user_id = user[0]
    day = user[1]

    info = get_db().execute(
        'SELECT i.event_id,title,subtitle,info_date,info_time,location,headword,short_description,low_temp,high_temp,event_details'
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

    return render_template('infoPage.html', user=user, info=info)


@bp.route('/<string:user_id_hashid>/<string:day_hashid>/survey', methods=['GET', 'POST'])
def get_survey(user_id_hashid, day_hashid):
    """Send survey

    According to a user's id and treatment group.
    Hash the user_id and day.
    """
    # if request.method == 'POST':
    #     uni = request.form['uni']
    #     error = None
    #
    #     if not uni:
    #         error = 'Please fill in your university.'
    #
    #     if error is not None:
    #         flash(error)
    #     else:
    #         db = get_db()
    #         db.execute(
    #             'INSERT INTO survey (user_id, result, created)'
    #             ' VALUES (?, ?, ?)',
    #             (user_id, uni, now)
    #         )
    #         db.commit()
    #         return render_template('finished.html')
    user = get_db().execute(
        'SELECT user_id, day'
        ' FROM user u'
        ' WHERE u.user_id_hashid = ? AND u.day_hashid = ?',
        (user_id_hashid, day_hashid,)
    ).fetchone()
    user_id = user[0]
    day = user[1]
    return render_template('survey' + str(day) + '.html')

@bp.route('/')
def index():
    return '谢谢参与！'

@bp.route('/completion/detail')
def completion():
    """Show all the users, and all results."""
    db = get_db()
    users = db.execute(
        'SELECT u.id, u.user_id, u.day, created'
        ' FROM user u JOIN survey s ON u.user_id = s.user_id'
        # TODO change to curr_time in activity
        ' ORDER BY created ASC'
    ).fetchall()
    return render_template('completion.html', users=users)

@bp.route('/survey7')
def survey7():
    return render_template('survey7.html')
