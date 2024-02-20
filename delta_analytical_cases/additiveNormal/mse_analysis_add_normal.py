import random
import numpy as np
import normal_additive
from SALib.sample import latin
from SALib.analyze import delta
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt



SEED = 230300
np.random.seed(SEED)
random.seed(SEED)

'''
The idea is to run the estimate for a quite big number of input (5) on different number of
samples to make the estimate: the true value is know: 
-see how the estimates' trajectories go
-evaluate the MSE
'''

mu = 0
sigma = 1
N = 5
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


samples = [100,500,1000,1500,2000,5000,10000]
estimates = np.zeros((N, len(samples)))
true_value = model.true_delta()*np.ones(len(samples))

iter = 0
for n_s in samples:
    param_values = latin.sample(problem, 1000, )
    Y = model.evaluate(param_values)
    delta_i = delta.analyze(problem,param_values,Y,print_to_console=False)['delta']
    estimates[:,iter] = delta_i
    iter = iter+1

mse = np.zeros(N)

for i in range(N):
    mse[i] = mean_squared_error(estimates[i,:],true_value)


y1 = estimates[0,:]
y2 = estimates[1,:]
y3 = estimates[2,:]
y4 = estimates[3,:]
y5 = estimates[4,:]


plt.figure(figsize=(8, 6))
plt.scatter(samples, y1, label='x1')
plt.scatter(samples, y2, label='x2')
plt.scatter(samples, y3, label='x3')
plt.scatter(samples, y4, label='x4')
plt.scatter(samples, y5, label='x5')

plt.plot(samples, y1, linestyle='-', marker='')
plt.plot(samples, y2, linestyle='-', marker='')
plt.plot(samples, y3, linestyle='-', marker='')
plt.plot(samples, y4, linestyle='-', marker='')
plt.plot(samples, y5, linestyle='-', marker='')

plt.axhline(y=model.true_delta(), color='r', linestyle='--', label='True delta value')
plt.xlabel('Number of samples in the estimate')
plt.ylabel('Delta index estimate')
plt.title('Normal input - Additive model')
plt.legend()
plt.xlim(0,max(samples))
plt.ylim(0, 0.3)

plt.show()


print('mse: ', mse)











