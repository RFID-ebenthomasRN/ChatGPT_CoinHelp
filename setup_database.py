import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('coin_flip_app.db')

c = conn.cursor()

# Create tables
# Table for coin flips
c.execute('''CREATE TABLE IF NOT EXISTS coin_flips (id INTEGER PRIMARY KEY AUTOINCREMENT, flip TEXT NOT NULL);''')

# Table for model predictions
c.execute('''CREATE TABLE IF NOT EXISTS model_predictions (id INTEGER PRIMARY KEY AUTOINCREMENT, model_name TEXT NOT NULL, prediction TEXT NOT NULL);''')

# Table for accuracy metrics
c.execute('''CREATE TABLE IF NOT EXISTS accuracy_metrics (id INTEGER PRIMARY KEY AUTOINCREMENT, model_name TEXT NOT NULL, session_accuracy REAL, all_time_accuracy REAL);''')

# Commit changes and close connection
conn.commit()
conn.close()