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

@bp.route('/test', methods=['GET', 'POST'])
def xian_info():
    return 'test'
