#!/bin/bash

gunicorn config.wsgi:application --log-level=info --log-file -