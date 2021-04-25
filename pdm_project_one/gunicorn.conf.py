#!/usr/bin/env python

command = '/Users/drewmac/webdev/pdm_project_one/.venv/bin/gunicorn'
pythonpath = '/Users/drewmac/webdev/pdm_project_one/pdm_project_one/'
bind = '127.0.0.1:8000'
workers = 1
worker_class = 'uvicorn.workers.UvicornWorker'
user = 'drewmac'
chdir = '/Users/drewmac/webdev/pdm_project_one/pdm_project_one'
