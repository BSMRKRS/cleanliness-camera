#!/bin/sh sh

sudo /etc/init.d/nginx start
python /home/pi/cleanliness/cleanliness_camera.py
