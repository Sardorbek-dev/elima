import sqlite3
import shutil
import os

# Path to your database file
db_path = 'db.sqlite3'  # Change this if your DB is named differently
backup_path = 'elima.backup_db.sqlite3'  # Desired backup file name

# Create a backup
shutil.copyfile(db_path, backup_path)

print(f"Backup of {db_path} created at {backup_path}")
