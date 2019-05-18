from urllib.parse import quote_plus
from os import environ, path

# Statement for enabling the development environment
DEBUG = bool(environ.get('FLASK_DEBUG', False))

# Define the application directory
BASE_DIR = path.abspath(path.dirname(__file__))


def get_database_uri():
    params = {
        'driver': environ.get('DB_ODBC_DRIVER', '{ODBC Driver 17 for SQL Server}'),
        'server': environ.get('DB_SERVER', '192.168.0.200'),
        'port': environ.get('DB_PORT', '1433'),
        'uid': environ.get('DB_USERNAME', 'sa'),
        'pwd': environ.get('DB_PASSWORD', 'raduguiF1re@'),
        'database': environ.get('DB_NAME', 'sis'),
    }

    schema = 'mssql+pyodbc'
    url_format = 'DRIVER={driver};SERVER={server},{port};DATABASE={database};UID={uid};PWD={pwd}'.format(**params)
    quoted_url = quote_plus(url_format)
    uri = '{schema}:///?odbc_connect={url}'.format(schema=schema, url=quoted_url)

    return uri


# Define the database
SQLALCHEMY_DATABASE_URI = get_database_uri()
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
