import numpy as np


class unif_add():
    '''
    Simple class to define a uniform additive model, with uniform in the d-dimensional hypercube
    '''

    def __init__(self,N,a,standard=True):
        self.N = N                  #number of inputs
        self.a = a                  #coefficients of linear combination
        self.standard = standard

    def get_dim(self):
        return self.N


    def evaluate(self,x):
        '''Evaluating the model'''
        return np.array([np.dot(self.a,x[i]) for i in range(x.shape[0])])

    def true_delta(self):

        if not self.standard:
            return None

        if self.N == 2:
            return 0.333
        if self.N == 3:
            return 0.228
        if self.N == 4:
            return 0.186
        if self.N == 5:
            return 0.166
        if self.N == 6:
            return 0.149
        if self.N == 10:
            return 0.113
        if self.N == 100:
            return 0.032
        if self.N == 1000:
            return 0.0088

