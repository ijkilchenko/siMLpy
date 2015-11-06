'''
@author: @ijkilchenko
'''

import unittest
import math
import random
from Algorithms import euclid, kmeanspp

class Test(unittest.TestCase):

    def test_Algorithms_euclid(self):
        fn = euclid()
        self.assertEqual(fn(5, 5), 0)
        self.assertEqual(fn([6], [6]), 0)
        self.assertEqual(fn([0, 0], [2, 0]), 2)
        self.assertEqual(fn(0, 1), 1)
        self.assertEqual(fn(10, 20), 10)
        self.assertEqual(fn([0, 0], [1, 1]), math.sqrt(2))
        self.assertEqual(fn([0, 0, 0], [1, 1, 1]), math.sqrt(3))
        self.assertEqual(fn(10, 20), fn(20, 10))
        self.assertEqual(fn(-5, 200), fn(200, -5))
        
    def test_Algorithms_kmeanspp(self):
        k = 10
        X = [[random.uniform(a, a + 1) for _ in range(10)] for a in range(0, 1000, math.floor(1000 / k))]
        X = [item for sublist in X for item in sublist]
        random.shuffle(X)
        L = kmeanspp(X, k, tol=10 ** -5, iter_max=10 ** 5)
        sums = [L.count(i) for i in range(k)]
        for i in range(len(sums) - 1):
            self.assertEqual(sums[i], sums[i + 1])
            
        k = 10
        X = [[(random.uniform(a, a + 1), random.uniform(a, a + 1)) for _ in range(10)] for a in range(0, 1000, math.floor(1000 / k))]
        X = [item for sublist in X for item in sublist]
        random.shuffle(X)
        L = kmeanspp(X, k, tol=10 ** -5, iter_max=10 ** 5)
        sums = [L.count(i) for i in range(k)]
        for i in range(len(sums) - 1):
            self.assertEqual(sums[i], sums[i + 1])

if __name__ == "__main__":
    unittest.main()
