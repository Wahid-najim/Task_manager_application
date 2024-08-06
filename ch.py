import sqlite3
import os
from werkzeug.security import generate_password_hash

# Define the directory and file path
dir_path = r'C:\Users\User\Documents\Task Maneger application\instance'
db_path = os.path.join(dir_path, 'task_manager.db')

# Create the directory if it does not exist
os.makedirs(dir_path, exist_ok=True)

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the User table
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Define the username and password
username = 'wahid'
password = 'fuck'

# Hash the password
hashed_password = generate_password_hash(password, method='sha256')

# Insert the user into the User table
try:
    cursor.execute('''
    INSERT INTO User (username, password)
    VALUES (?, ?)
    ''', (username, hashed_password))
    print("User added successfully!")
except sqlite3.IntegrityError:
    print("User already exists!")

# Commit changes and close the connection
conn.commit()
conn.close()
