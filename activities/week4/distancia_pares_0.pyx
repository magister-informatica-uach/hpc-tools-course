import numpy as np

def distancia_pares(data):    
    N, D = data.shape
    dist = np.zeros(shape=(N, N))
    for i in range(N):
        for j in range(i+1, N):
            for k in range(D):
                dist[i, j] += (data[i, k] - data[j, k])**2
            dist[i, j] = np.sqrt(dist[i, j])
            dist[j, i] = dist[i, j]
    return dist

