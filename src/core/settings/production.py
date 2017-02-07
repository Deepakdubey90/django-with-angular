import os
import json
import dj_database_url

SECRET_KEY = 'mp#6zm!kuakjln$_5kts5fyq5%z16z$mj6bt0n58)wr!^#z^hb'

DEBUG = False

connection = dj_database_url.parse(os.environ.get("DATABASE_URL"))
connection.update({
    'CONN_MAX_AGE': 600,
})
DATABASES = {
    "default": connection,
}

ALLOWED_HOSTS = [os.environ.get("HOST", "*"), ]
