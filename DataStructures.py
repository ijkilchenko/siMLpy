'''
@author: @ijkilchenko
'''

class MlList(list):
    '''
    MlList
    '''
    
    def __init__(self):
        super().__init__(self)
    
    def cluster(self, k, **kwargs):
        if 'fn' in kwargs:
            fn = kwargs['fn']
        else:
            fn = 'euclid'
        if 'alg' in kwargs:
            alg = kwargs['alg']
        else:
            alg = 'kmeans++'
    