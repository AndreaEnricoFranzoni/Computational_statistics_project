import numpy as np
import matplotlib.pyplot as plt
import SALib
from SALib import ProblemSpec
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import oakley2004
from hand_made import A
from hand_made import M
from SALib.plotting.bar import plot as barplot


#instance of the problem
problem={
    'num_vars': 15,
    'names': ["x{}".format(i) for i in range(1, 16)],
    'bounds': [
            [0.0, 1.0],
        ]
        * 15,
    'dists': ["norm"] * 15,
}


#Generate samples
param_values = saltelli.sample(problem,1000,)

#Evaluate output
Y = oakley2004.evaluate(param_values,A,M)

#Compute indices
S_i = sobol.analyze(problem,Y,print_to_console=True)
#returns first, second and total order, with CIs
total_Si, first_Si, second_Si = S_i.to_df()

#plotting
#first order
fig, ax1 = plt.subplots(1,1, figsize=(12,6))
ax1 = barplot(first_Si, ax=ax1)
ax1.set_xlabel("Inputs")
ax1.set_ylabel("First order Sobol indices")
plt.show()

#second order: useless plot
#fig, ax1 = plt.subplots(1,1, figsize=(12,6))
#ax1 = barplot(second_Si, ax=ax1)
#ax1.set_xlabel("Parameters")
#ax1.set_ylabel("Second order Sobol indices")
#plt.show()

#total
fig, ax1 = plt.subplots(1,1, figsize=(12,6))
ax1 = barplot(total_Si, ax=ax1)
ax1.set_xlabel("Inputs")
ax1.set_ylabel("Total effect Sobol indices")
plt.show()



