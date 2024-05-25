def mse(true, pred, N):
    sum = 0
    for i in range(N):
        sum += (true[i] - pred[i]) ** 2
    return sum / N

def rmse(true, pred, N):
    return mse(true, pred, N) ** 0.5

