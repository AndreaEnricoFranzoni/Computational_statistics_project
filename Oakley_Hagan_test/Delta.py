import numpy as np
import matplotlib.pyplot as plt
from SALib.sample import latin
from SALib.analyze import delta
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
param_values = latin.sample(problem,1000,)

#Run model
Y = oakley2004.evaluate(param_values,A,M)

#Analysis
delta_i = delta.analyze(problem,param_values,Y,print_to_console=True)
delta_indices = delta_i.to_df()[['delta','delta_conf']]

#plotting
fig, ax1 = plt.subplots(1,1, figsize=(12,6))
ax1 = barplot(delta_indices, ax=ax1)
ax1.set_xlabel("Inputs")
ax1.set_ylabel("Delta value")
plt.show()
