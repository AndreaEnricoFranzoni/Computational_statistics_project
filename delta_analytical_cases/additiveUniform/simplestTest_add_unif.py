import numpy as np
import uniform_additive
import random
from SALib.sample import latin
from SALib.analyze import delta


SEED = 230300
np.random.seed(SEED)
random.seed(SEED)

'''
Script to simple test the model
'''
N = 10
a = np.ones(N)

model = uniform_additive.unif_add(N,a)

problem={
    'num_vars': N,
    'names': ["x{}".format(i) for i in range(1, N+1)],
    'bounds': [
            [0, 1],
        ]
        * N,
    'dists': ["unif"] * N,
}



#Generate samples
param_values = latin.sample(problem,1000,)

#Run model
Y = model.evaluate(param_values)

#Analysis
delta_i = delta.analyze(problem,param_values,Y,
                    print_to_console=True)

