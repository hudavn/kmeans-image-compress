import numpy as np
import sklearn.cluster

def kmeans(X, k):
    centers = X[np.random.choice(X.shape[0], k, replace = False)]
    labels = []

    print("\n--- [INFO] Processing...")
    
    while True:
        _X = X * np.ones((k,1,1))
        _centers = centers.reshape(centers.shape[0], 1, centers.shape[1])
        labels = np.argmin(
                    np.sqrt(
                        np.sum(
                            np.square(_X - _centers),
                            axis=2)
                        )
                    , axis=0)

        new_centers = np.zeros((k, X.shape[1]))

        for i in range(k):
            new_centers[i] = np.mean(X[labels == i], axis=0)

        if (set([tuple(a) for a in centers]) == set([tuple(a) for a in new_centers])):
            break
        else:
            centers = new_centers

    # evaluator = sklearn.cluster.KMeans(n_clusters=k).fit(X)
    # print(evaluator.cluster_centers_)
    return centers, labels

  
