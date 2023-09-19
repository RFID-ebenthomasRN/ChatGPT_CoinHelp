# CoinFlipAppGUI.py
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar


class CoinFlipAppGUI:
    def __init__(self, master, submit_callback):
        self.master = master

        # Label for running tally
        self.tally_label = tk.Label(master, text='Running Tally')
        self.tally_label.pack()

        # Buttons for Heads and Tails
        self.heads_button = tk.Button(master, text='Heads', command=lambda: submit_callback('H'))
        self.heads_button.pack()
        self.tails_button = tk.Button(master, text='Tails', command=lambda: submit_callback('T'))
        self.tails_button.pack()

        # Matplotlib Graph
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack()

        # Dropdown Calendar
        self.cal = Calendar(master)
        self.cal.pack()

        # Frequency of Accurate Predictions
        self.freq_label = tk.Label(master, text='Frequency of Accurate Predictions')
        self.freq_label.pack()

        # Display of each model's guess and a consensus guess
        self.model_guess_label = tk.Label(master, text='Model Guesses')
        self.model_guess_label.pack()

        # Session and all-time accuracy percentages for each model
        self.accuracy_label = tk.Label(master, text='Model Accuracy')
        self.accuracy_label.pack()