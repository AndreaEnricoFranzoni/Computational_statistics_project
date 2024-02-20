import numpy as np
import lognormal_multiadditive
import random
from SALib.sample import latin
from SALib.analyze import delta
import matplotlib.pyplot as plt


SEED = 230300
np.random.seed(SEED)
random.seed(SEED)

'''
Since the results with the multiplicative lognormal method were quite strange:
try with different values of number of parameters
'''
eta = 1
sigma = 1

N = [2,3,4,5,6,10]
mean_estimate = [0]*len(N)
true_values = [0]*len(N)

iter = 0
for n in N:

    a = np.ones(n)

    model = lognormal_multiadditive.log_nor_mul(eta, sigma, n, a)

    problem = {
        'num_vars': n,
        'names': ["x{}".format(i) for i in range(1, n + 1)],
        'bounds': [
                      [eta, sigma],
                  ]
                  * n,
        'dists': ["lognorm"] * n,
    }

    # Generate samples
    param_values = latin.sample(problem, 1000, )

    # Run model
    Y = model.evaluate(param_values)

    # Analysis
    delta_i = delta.analyze(problem, param_values, Y,
                            print_to_console=False)['delta']

    mean_estimate[iter] = np.mean(delta_i)
    true_values[iter] = model.true_delta()
    iter = iter+1


plt.figure(figsize=(8, 6))
plt.scatter(N, mean_estimate, label='Mean delta estimate')
plt.scatter(N, true_values, label='True delta value', s=50)

plt.plot(N, mean_estimate, linestyle='-', marker='')

plt.xlabel('Number of inputs')
plt.ylabel('Delta')
plt.title('Estimate of delta index vs number of inputs')
plt.legend()
plt.xlim(0,max(N)+1)
plt.ylim(0, 1)

plt.show()

f = 0