#!/usr/bin/env python
command = '/apps/wbdesigner/.venv/bin/gunicorn'
pythonpath = '/apps/wbdesigner/pdm_project_one'
bind = '127.0.0.1:8000'
workers = 4
worker_class = 'uvicorn.workers.UvicornWorker'
user = 'wbduser'
chdir = '/apps/wbdesigner/pdm_project_one'
