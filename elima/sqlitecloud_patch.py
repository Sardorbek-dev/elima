import sqlite3
import sqlitecloud

_orig_connect = sqlite3.connect

def cloud_connect(*args, **kwargs):
    # Django will call sqlite3.connect(database=NAME, **other)
    url = kwargs.pop('database', args[0] if args else None)
    return sqlitecloud.connect(url)

sqlite3.connect = cloud_connect
