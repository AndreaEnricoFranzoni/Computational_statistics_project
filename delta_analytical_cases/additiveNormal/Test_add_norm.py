import numpy as np
import normal_additive
from SALib.sample import latin
from SALib.analyze import delta
import random

SEED = 230300
np.random.seed(SEED)
random.seed(SEED)

'''
Simple script to try the class
'''

mu = 0
sigma = 1
N = 10
a = np.ones(N)

model = normal_additive.normal_add(mu,sigma,N,a)

problem={
    'num_vars': N,
    'names': ["x{}".format(i) for i in range(1, N+1)],
    'bounds': [
            [mu, sigma],
        ]
        * N,
    'dists': ["norm"] * N,
}



#Generate samples
param_values = latin.sample(problem,1000,)

#Run model
Y = model.evaluate(param_values)

#Analysis
delta_i = delta.analyze(problem,param_values,Y,
                    print_to_console=True)

