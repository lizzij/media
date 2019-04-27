# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# import functools
#
# from datetime import datetime
#
# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, session, url_for
# )
#
# from media.db import get_db
# from werkzeug.exceptions import abort
#
# bp = Blueprint('survey', __name__)
# now = datetime.now()
#
# @bp.route('/<string:user_id_hashid>/<string:day_hashid>/survey', methods=['GET', 'POST'])
# def get_consent(user_id_hashid, day_hashid):
#     """Record consent
#
#     According to a user's id and treatment group.
#     Hash the user_id and day.
#     """
#     user = get_db().execute(
#         'SELECT user_id, day'
#         ' FROM user u'
#         ' WHERE u.user_id_hashid = ? AND u.day_hashid = ?',
#         (user_id_hashid, day_hashid,)
#     ).fetchone()
#     if user is None:
#         abort(404, "User {0}/{1} doesn't exist.".format(user_id_hashid, day_hashid))
#     user_id = user[0]
#     day = user[1]
#
#     if request.method == 'POST':
#         consent = request.form['consent']
#         error = None
#
#         db = get_db()
#         db.execute(
#             'INSERT INTO survey (user_id, result, created)'
#             ' VALUES (?, ?, ?)',
#             (user_id, consent, now)
#         )
#         db.commit()
#         flash("Recorded: user %s result %s at %s" % (user_id, consent, now))
#     # user = get_db().execute(
#     #     'SELECT user_id, day'
#     #     ' FROM user u'
#     #     ' WHERE u.user_id_hashid = ? AND u.day_hashid = ?',
#     #     (user_id_hashid, day_hashid,)
#     # ).fetchone()
#     # user_id = user[0]
#     # day = user[1]
#     # return render_template('survey' + str(day) + '.html')
