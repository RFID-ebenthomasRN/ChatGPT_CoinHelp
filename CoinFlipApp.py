# CoinFlipApp.py
import tkinter as tk
from DQN import DQN
from BayesianPredictor import BayesianPredictor
from FrequencyPredictor import FrequencyPredictor
from LSTMPredictor import LSTMPredictor
from CoinFlipAppGUI import CoinFlipAppGUI
import sqlite3

class CoinFlipApp:
    def __init__(self, master):
        self.master = master
        self.coin_flips = []
        self.dqn = DQN(1, 2)
        self.bayesian = BayesianPredictor()
        self.frequency = FrequencyPredictor()
        self.lstm = LSTMPredictor()
        self.gui = CoinFlipAppGUI(master, self.submit)
        self.conn = sqlite3.connect('coinflip.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS flips (flip TEXT)''')
        print('Table flips should be created now.')
        self.conn.commit()

    def submit(self, flip):
        print(f'Button pressed: {flip}')
        self.coin_flips.append(flip)
        self.c.execute("INSERT INTO flips VALUES (?)", (flip,))
        self.conn.commit()
        numerical_flips = [1 if x == 'H' else 0 for x in self.coin_flips]
        dqn_pred = self.dqn.predict(numerical_flips)
        bayesian_pred = self.bayesian.predict(numerical_flips)
        freq_pred = self.frequency.predict(numerical_flips)
        lstm_pred = self.lstm.predict(numerical_flips)
        self.gui.update_predictions(dqn_pred, bayesian_pred, freq_pred, lstm_pred)

    def update_prediction(self):
        self.c.execute("SELECT * FROM flips")
        historical_data = self.c.fetchall()
        # Update logic here, including database queries and model predictions

if __name__ == '__main__':
    root = tk.Tk()
    app = CoinFlipApp(root)
    root.mainloop()