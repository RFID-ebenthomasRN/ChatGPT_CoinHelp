from keras.models import Sequential
from keras.layers import Dense
import numpy as np

class DQN:
    def __init__(self, input_dim, output_dim):
        self.model = Sequential()
        self.model.add(Dense(24, input_dim=input_dim, activation='relu'))
        self.model.add(Dense(24, activation='relu'))
        self.model.add(Dense(output_dim, activation='linear'))
        self.model.compile(loss='mse', optimizer='adam')

    def train(self, state, action, reward, next_state, done):
        target = reward
        if not done:
            target = (reward + 0.95 * np.amax(self.model.predict(next_state)[0]))
        target_f = self.model.predict(state)
        target_f[0][action] = target
        self.model.fit(state, target_f, epochs=1, verbose=0)

    def predict(self, state):
        return self.model.predict(state)