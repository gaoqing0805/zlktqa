#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: decorators.py
Author: cyan
Time: 2019/7/31 19:57
Desc: 
"""
# 登录限制的装饰器
from flask import redirect, url_for, session
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper