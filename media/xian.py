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

def get_event(event_id, cohort):
    info = get_db().execute(
        'SELECT i.event_id,title,subtitle,info_date,info_time,location,image_file,short_description,low_temp,high_temp,suitable_for_family,suitable_for_friends,suitable_for_lover,suitable_for_baby,suitable_for_elderly,suitable_for_pet,event_details,phrase_for_week, phrase_for_day, phrase_for_header'
        ' FROM infos i'
        ' WHERE i.event_id = ? AND cohort = ?',
        (event_id, cohort,)
    ).fetchone()
    return info

@bp.route('/<string:user_id_hashid>/<string:day_hashid>/info', methods=['GET', 'POST'])
def get_info(user_id_hashid, day_hashid):
    user = get_user(user_id_hashid, day_hashid)
    user_id = user[0]
    day = user[1]
    treatment = user[2]
    if day == 1:
        info = get_event(1, 1)
        template = 'a'
    elif day == 2:
        info = get_event(2, 1)
        template = 'c'
    render_template('xian/infoPage' + template + '.html', info=info, day=day, treatment=treatment)
