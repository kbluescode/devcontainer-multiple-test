#!/usr/bin/bash

gunicorn -b 0.0.0.0 wsgi:app
