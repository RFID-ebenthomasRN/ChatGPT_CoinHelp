import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BayesianPredictor:
    @staticmethod
    def predict(data):
        try:
            heads = data.count(0)
            tails = data.count(1)
            total = heads + tails
            if total == 0:
                logging.warning('No data available for prediction.')
                return None

            prediction = 0 if heads / total > tails / total else 1
            logging.info(f'Bayesian prediction made: {prediction}')
            return prediction
        except Exception as e:
            logging.error(f'An error occurred during Bayesian prediction: {e}')
            return None