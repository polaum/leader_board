import os

def _set_env_var(name, default):
    try:
        return os.environ[name]
    except KeyError:
        return default

HOST = _set_env_var('HOST', '0.0.0.0')
PORT = _set_env_var('PORT', 3000)
DB_URL = _set_env_var('DB_URL', 'postgresql://localhost:5432/leader_board')
