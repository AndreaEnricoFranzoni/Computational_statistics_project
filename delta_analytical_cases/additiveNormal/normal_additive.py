import numpy as np


class normal_add():

    '''
    Simple class to define a normal additive model
    '''

    def __init__(self,mu,sigma,N,a,standard=True):
        self.mu = mu                #mean of each input (we assume it is the same)
        self.sigma = sigma          #variance of each input (we assume it is the same for each input)
        self.N = N                  #number of inputs
        self.a = a                  #coefficients of linear combination
        self.standard = standard    #true is all the inputs are normal gaussian

    def get_dim(self):
        return self.N

    def evaluate(self,x):
        '''
        Function to evaluate the output
        '''
        return np.array([np.dot(self.a,x[i]) for i in range(x.shape[0])])

    def true_delta(self):
        '''
        Known values of delta index for a standard model, with a given number of inputs
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
            return 0.0088

