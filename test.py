import pandas as pd
class cal:
    def __init__(self, lines):
        self.lines = lines
        self.data_count = len(lines) - 1

    def mse(self):
        sum = 0
        for i, values in enumerate(self.lines):
            if i != 0:
                (y_trues, y_preds) = values.split(',')
                sum += (float(y_trues)-float(y_preds))**2

        return sum / self.data_count