import numpy as np


class log_nor_mul():
    '''
    Simple class to define a multiplicative lognormal model
    '''

    def __init__(self,eta,sigma,N,a,standard=True):
        self.eta = eta              #mean of ln(x_i) (we assume it equal for each one of the inputs)
        self.sigma = sigma          #variance of ln(x_i) (we assume it equal for each one of the inputs)
        self.N = N                  #number of inputs
        self.a = a                  #exponents
        self.standard = standard    #if all the inputs are st mean and variance of ln(x_i) are both 1

    def get_dim(self):
        return self.N

    def single_eval(self,m):

        res = 1

        for i in range(self.N):
            res = res*(m[i]**self.a[i])

        return res



    def evaluate(self,x):
        '''
        Simply evaluating the model
        '''
        return np.array([self.single_eval(x[i]) for i in range(x.shape[0])])

    def true_delta(self):
        '''
        True values of the delta_i if we have a standard model and a given number of inputs
        '''

        if not self.standard:
            return None

        if self.N == 2:
            return 0.306
        if self.N == 3:
            return 0.224
        if self.N == 4:
            return 0.185
        if self.N == 5:
            return 0.16
        if self.N == 6:
            return 0.144
        if self.N == 10:
            return 0.107
        if self.N == 100:
            return 0.032
        if self.N == 1000:
            return 0.032

