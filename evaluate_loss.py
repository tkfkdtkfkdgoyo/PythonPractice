import loss as loss
import pandas as pd

loss_test = pd.read_csv('/Users/jumalgom/PycharmProjects/PythonPractice/13.quiz_data.csv')

y_trues = loss_test['y_trues'] # 열 이름이 y_trues인 데이터를 가져옴
y_preds = loss_test['y_preds'] # 열 이름이 y_preds인 데이터를 가져옴

y_trues_list = y_trues.tolist() # y_trues를 리스트로 변환
y_preds_list = y_preds.tolist() # y_preds를 리스트로 변환

N = len(y_trues_list) # y_trues_list의 길이를 N에 저장

# round 함수를 사용하여 소수점 둘째 자리까지 출력
print("MSE:", round(loss.mse(y_trues_list, y_preds_list, N), 2)) # MSE 함수를 호출하여 출력
print("RMSE:", round(loss.rmse(y_trues_list, y_preds_list, N), 2)) # RMSE 함수를 호출하여 출력



