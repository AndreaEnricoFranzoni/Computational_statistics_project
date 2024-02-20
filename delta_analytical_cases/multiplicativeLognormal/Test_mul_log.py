import numpy as np
import lognormal_multiadditive
import random
from SALib.sample import latin
from SALib.analyze import delta

SEED = 230300
np.random.seed(SEED)
random.seed(SEED)

'''
Simple script to try the class
'''


eta = 1
sigma = 1
N = 5
a = np.ones(N)

model = lognormal_multiadditive.log_nor_mul(eta,sigma,N,a)

problem={
    'num_vars': N,
    'names': ["x{}".format(i) for i in range(1, N+1)],
    'bounds': [
            [eta, sigma],
        ]
        * N,
    'dists': ["lognorm"] * N,
}



#Generate samples
param_values = latin.sample(problem,1000,)

#Run model
Y = model.evaluate(param_values)

#Analysis
delta_i = delta.analyze(problem,param_values,Y,
                    print_to_console=True)
