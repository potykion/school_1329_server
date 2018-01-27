# About

[![Build Status](https://travis-ci.org/potykion/school_1329_server.svg?branch=master)](https://travis-ci.org/potykion/school_1329_server)

Server for School 1329 App.

API docs can be found [here](https://github.com/potykion/school_1329_server/wiki).

# Deploy

- Install pipenv:
    ```
    pip install pipenv
    ```

- Install requirements:
    ```
    pipenv install -r requirements.txt
    ```

- Apply migrations:
    ```
    pipenv run python manage.py migrate
    ```

- Collect and upload static to GCS:
    ```
    python manage.py collectstatic
    gsutil rsync -R static/ gs://sch1329
    ```

- Deploy to GAE:
    ```
    gcloud app deploy
    ```

