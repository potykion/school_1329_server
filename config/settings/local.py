import dj_database_url

from .common import *

DEBUG = True

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3'
    )
}
