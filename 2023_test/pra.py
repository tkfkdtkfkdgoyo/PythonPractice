import pandas as pd


class MyMath:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)
        self.data_count = len(self.data)

    def cal_mse(self):
        mse = ((self.data['y_trues'] - self.data['y_preds']) ** 2).mean()
        return mse

    def cal_rmse(self):
        mse = self.cal_mse()
        rmse = mse ** 0.5
        return rmse


# 파일 경로를 사용하여 데이터 읽기
filepath = 'prediction_data.csv'
prediction = MyMath(filepath)
print('mse: {:.2f}'.format(prediction.cal_mse()))
print('rmse: {:.2f}'.format(prediction.cal_rmse()))
