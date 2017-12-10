# About

[![Build Status](https://travis-ci.org/potykion/school_1329_server.svg?branch=master)](https://travis-ci.org/potykion/school_1329_server)

Server for School 1329 App. API docs can be found [here](https://github.com/potykion/school_1329_server/wiki/School-1329-API).

# Local development

## Setup:
- Soft: Python version: 3.5+; virtualenv
- Dependencies: ```pip install requirements.txt```
- Local env settings: ```set DJANGO_SETTINGS_MODULE=config.settings.local``` (Linux/Mac: ```export DJANGO_SETTINGS_MODULE=config.settings.local```)
- Apply migrations: ```python manage.py migrate```

## Commands:
- To run server: ```python manage.py runserver```
- To run tests: ```pytest tests```
