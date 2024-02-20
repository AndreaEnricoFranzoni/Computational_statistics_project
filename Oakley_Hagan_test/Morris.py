import numpy as np
import matplotlib.pyplot as plt
import SALib
from SALib.sample import morris
from SALib.analyze import morris
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

#samples
param_values = SALib.sample.morris.morris.sample(problem,10,)
#Interesting: infinite values are produced: produces as starting point some infinite values:
# the sin functions cannot be evaluated there: does not give back results

#Run model
Y = oakley2004.evaluate(param_values,A,M)

#Analysis
ee_i = morris.analyze(problem,param_values,Y,print_to_console=True)

#plotting
fig, ax1 = plt.subplots(1,1, figsize=(12,6))
ax1 = barplot(ee_i.to_df(), ax=ax1)
ax1.set_xlabel("Inputs")
ax1.set_ylabel("Delta value")
plt.show()


