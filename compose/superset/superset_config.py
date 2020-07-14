from celery.schedules import crontab

# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------

ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088

SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

SQLALCHEMY_DATABASE_URI = "postgresql://superset:superset@superset-db/superset"

# ---------------------------------------------------------
# Flask App Builder configuration
# ---------------------------------------------------------

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# ---------------------------------------------------------
# Cache configuration
# ---------------------------------------------------------


CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60 * 24,  # 1 day default (in secs)
    "CACHE_KEY_PREFIX": "superset_results",
    "CACHE_REDIS_URL": "redis://superset-cache:6379/2",
}


class CeleryConfig(object):
    BROKER_URL = "redis://superset-cache:6379/2"
    CELERY_IMPORTS = (
        "superset.sql_lab",
        "superset.tasks",
    )
    CELERY_RESULT_BACKEND = "redis://superset-cache:6379/2"
    CELERYD_LOG_LEVEL = "DEBUG"
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True
    CELERY_ANNOTATIONS = {
        "sql_lab.get_sql_results": {"rate_limit": "100/s", },
        "email_reports.send": {
            "rate_limit": "1/s",
            "time_limit": 120,
            "soft_time_limit": 150,
            "ignore_result": True,
        },
    }
    CELERYBEAT_SCHEDULE = {
        "email_reports.schedule_hourly": {
            "task": "email_reports.schedule_hourly",
            "schedule": crontab(minute=1, hour="*"),
        },
        "cache-warmup-hourly": {
            "task": "cache-warmup",
            "schedule": crontab(minute=0, hour="*"),  # hourly
            "kwargs": {
                "strategy_name": "top_n_dashboards",
                "top_n": 5,
                "since": "7 days ago",
            },
        },
    }


CELERY_CONFIG = CeleryConfig

MAPBOX_API_KEY = "1"

# Uncomment to setup Your App name
APP_NAME = "Superset"

# Uncomment to setup an App icon
APP_ICON = "/static/assets/images/superset-logo@2x.png"
APP_ICON_WIDTH = 126

BABEL_DEFAULT_LOCALE = "zh"
BABEL_DEFAULT_FOLDER = "superset/translations"

LANGUAGES = {
    "zh": {"flag": "cn", "name": "Chinese"},
}

JINJA_CONTEXT_ADDONS = {
    "my_crazy_macro": lambda x: x * 2,
}
