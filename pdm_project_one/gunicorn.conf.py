#!/usr/bin/env python

command = '/home/azwerd/webapp/.venv/bin/gunicorn'
bind = '127.0.0.1:8000'
workers = 4
worker_class = 'uvicorn.workers.UvicornWorker'
user = 'azwerd'
chdir = '/home/azwerd/webapp/pdm_project_one'
