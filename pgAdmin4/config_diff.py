# Data directory for storage of config settings etc.
if IS_WIN:
    # Use the short path on windows
    DATA_DIR = os.path.realpath(
        os.path.join(fs_short_path(env('APPDATA')), "pgAdmin")
    )
else:
    if SERVER_MODE:
        ### Old data dir
        # DATA_DIR = '/var/lib/pgadmin'
        DATA_DIR = '/opt/pgadmin4/var/lib'
    else:
        DATA_DIR = os.path.realpath(os.path.expanduser('~/.pgadmin/'))
