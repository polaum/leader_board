import os

def _set_env_var(name, default):
    try:
        return os.environ[name]
    except KeyError:
        return default

SERVER_HOST = _set_env_var('SERVER_HOST', '0.0.0.0')
SERVER_PORT = _set_env_var('SERVER_PORT', 3000)
DB_URL = _set_env_var('DB_URL', 'postgresql://localhost:5432/leader_board')
