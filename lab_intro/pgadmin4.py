import os

SERVER_MODE = False
DEFAULT_SERVER = '127.0.0.1'
DEFAULT_SERVER_PORT = 5050
SQLITE_PATH = os.path.join(os.path.dirname(__file__), 'pgadmin4.db')
LOG_FILE = os.path.join(os.path.dirname(__file__), 'pgadmin4.log')
SESSION_DB_PATH = os.path.join(os.path.dirname(__file__), 'sessions')
STORAGE_DIR = os.path.join(os.path.dirname(__file__), 'storage')
