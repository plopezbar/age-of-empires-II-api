import os

DB_NAME = 'sqlite:///{}/db/data.db'.format(os.path.abspath("."))
API_PREFIX = "/api/v1"

APP_CONFIG = {
    'SQLALCHEMY_DATABASE_URI': DB_NAME,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'PROPAGATE_EXCEPTIONS': True,
    'JSONIFY_PRETTYPRINT_REGULAR': True,
    'JSON_SORT_KEYS': False,
    'SWAGGER': {
        'title': 'Age of Empires II API',
        'uiversion': 3
    }
}

SWAGGER_CONFIG = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json'
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
