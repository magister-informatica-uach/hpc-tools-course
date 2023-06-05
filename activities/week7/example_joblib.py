from joblib import Parallel, delayed
import numpy as np

def create_data(N):
    return np.random.randn(N)

def distancia_pares_numpy(data):
    return np.sqrt(np.sum((data.reshape(-1, 1, 2) - data.reshape(1, -1, 2))**2, axis=-1))


dataset = [create_data(1000) for k in range(5)]

print(Parallel(n_jobs=2)(delayed(distancia_pares_numpy)(data) for data in dataset))
