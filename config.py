import os

DB_NAME = 'sqlite:///{}/db/data.db'.format(os.path.abspath("."))
API_PREFIX = "/api/v1"

APP_CONFIG = {
    'SQLALCHEMY_DATABASE_URI': DB_NAME,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'PROPAGATE_EXCEPTIONS': True,
    'JSONIFY_PRETTYPRINT_REGULAR': True,
    'JSON_SORT_KEYS': False
}
