import sqlite3

# Initialize SQLite database
conn = sqlite3.connect('coin_flip_predictions.db')
c = conn.cursor()

def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        model_name TEXT,
        prediction TEXT,
        actual TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()

def insert_prediction(model_name, prediction, actual):
    c.execute("""INSERT INTO predictions (model_name, prediction, actual)
        VALUES (?, ?, ?)""", (model_name, prediction, actual))
    conn.commit()

def fetch_predictions():
    c.execute('SELECT * FROM predictions')
    return c.fetchall()

def main():
    create_tables()
    # Example usage
    insert_prediction('DQN', 'Heads', 'Tails')
    print(fetch_predictions())

if __name__ == '__main__':
    main()