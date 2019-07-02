# !/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

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
    return render_template('surveyList.html', surveys=surveys)

@bp.route('/allUsers')
def users():
    """Show all the surveys, and all results."""
    db = get_db()
    users = db.execute(
        'SELECT user_id, day, wechat_id, treatment, cohort, user_id_hashid, day_hashid'
        ' FROM user s'
        ' ORDER BY user_id ASC'
    ).fetchall()
    return render_template('userList.html', users=users)

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

@bp.route('/allEvents')
def all_events():
    """Show all the events."""
    db = get_db()
    events = db.execute(
        'SELECT * FROM infos ORDER BY info_id ASC'
    ).fetchall()
    return render_template('infoList.html', events=events)

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
    return render_template('updateEvent.html', info=info)

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
