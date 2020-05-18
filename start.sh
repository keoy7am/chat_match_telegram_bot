#!/bin/bash
now=$(date '+%Y-%m-%d %H:%M:%S')
echo "$now: staring bot..." >> boot.log
ls /volume/app -lh

mkdir /volume/app/logs
chown -R www-data:www-data /volume/app
chmod -R 775 /volume/app
usermod -u 1000 www-data

gunicorn -w 4 -k gevent --bind 0.0.0.0:5000 runserver:app -preload
