'''
@author: @ijkilchenko
'''

from math import sqrt
from collections import Iterable
from random import randint, random

def kmeanspp(X, k, **kwargs):
    '''
    Performs k-means on X into k clusters. Initialization of the k centroids is done via k-means++. 
    
    :param X: X is an iterable of iterables, e.g., [[1, 2], [3, 4]] or ((1), (2)). 
    :param k: number of clusters.
    :param kwargs['fn']: select a distance function (default is 'euclid') or provide your own.
    :param kwargs['tol']: clustering continues while the difference (under fn) between centroids at consecutive iterations is more than tol.
    :param kwargs['iter_max']: clustering continues at most iter_max times.  
    :return: returns an MlList L of length len(X) where each index i in L belongs to cluster L[i]. 
    '''
    
    assert len(X) >= k 
    
    dim = len(X[0]) if isinstance(X[0], Iterable) else 1

    if 'fn' in kwargs:
        fn = kwargs['fn']
    else:
        fn = euclid()
    if 'tol' in kwargs:
        tol = kwargs['tol']
    else:
        tol = 10 ** -3
    if 'iter_max' in kwargs:
        iter_max = kwargs['iter_max']
    else:
        iter_max = 10 ** 3
    
    def init_k_centroids(X, k, fn):
        centroids = []
        centroids.append(X[randint(0, len(X) - 1)])
        while len(centroids) < k:
            D = []
            for p in X:
                D_min = fn(p, centroids[0])
                for i in range(1, len(centroids)):
                    D_min_current = fn(p, centroids[i])
                    if D_min > D_min_current:
                        D_min = D_min_current
                D.append(D_min)
            S = sum(D)
            D = [d / S for d in D]
            r = random()
            
            i = 0
            while r > 0:
                r = r - D[i]
                i += 1
            centroids.append(X[i - 1])
        return centroids
    
    centroids = init_k_centroids(X, k, fn)
    
    def calc_centroid(L, i):
        n = sum([j == i for j in L])
        if dim > 1:
            return [sum([x[d] for j, x in enumerate(X) if L[j] == i]) / n for d in range(dim)]
        else:
            return sum([x for j, x in enumerate(X) if L[j] == i]) / n
        
    def get_nearest_centroid(x, centroids):
        (D_min, i) = (fn(x, centroids[0]), 0)
        for j in range(1, len(centroids)):
            D_min_current = fn(x, centroids[j])
            if D_min > D_min_current:
                (D_min, i) = (D_min_current, j)
        return i
        
    diff = tol + 1
    iter_count = 0
    while (diff > tol and iter_count < iter_max):
        L = [get_nearest_centroid(x, centroids) for x in X]
        centroids_new = [calc_centroid(L, i) for i in range(k)]
        diff = sum([fn(centroid, centroid_new) for centroid, centroid_new in zip(centroids, centroids_new)])
        centroids = centroids_new
        iter_count += 1
    return L

def euclid():
    '''
    Return a function which calculates the Euclidean distance between two iterables (points). 
    If either of two arguments to the function are not iterable, each are put in its own list first. 

    :return: returns the Euclidean distance function
    '''
    seq = lambda x, y: zip(x, y) if all(isinstance(z, Iterable) for z in [x, y]) else zip([x], [y])
    euc = lambda x, y: sqrt(sum([(p[0] - p[1]) ** 2 for p in seq(x, y)]))
    return euc

def demo():
    pass
