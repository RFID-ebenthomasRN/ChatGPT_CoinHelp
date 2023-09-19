from collections import Counter
import logging

# Initialize logging
logging.basicConfig(filename='frequency_predictor.log', level=logging.INFO)

# Frequency Prediction
class FrequencyPredictor:
    def __init__(self):
        self.data = []

    def update_data(self, flip):
        self.data.append(flip)

    def predict(self):
        try:
            most_common = Counter(self.data).most_common(1)[0][0]
            logging.info(f'Prediction made: {most_common}')
            return most_common
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            return None