#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: config.py
Author: cyan
Time: 2019/7/30 12:05
Desc: 
"""

import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlktqa'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE
)

SQLALCHEMY_DATABASE_URI = DB_URI

# SQLALCHEMY一旦发生变化，就去跟踪它的修改
SQLALCHEMY_TRACK_MODIFICATIONS = False
