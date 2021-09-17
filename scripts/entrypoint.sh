#!/bin/sh

set -e

uwsgi --socket :9000 --master --enable-threads --module app.wsgi

