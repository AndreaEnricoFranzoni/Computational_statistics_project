import numpy as np
import matplotlib.pyplot as plt
import SALib
from SALib.sample import fast_sampler
from SALib.analyze import fast
from SALib.test_functions import oakley2004
from hand_made import A
from hand_made import M
from SALib.plotting.bar import plot as barplot


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
param_values = fast_sampler.sample(problem,1000,)

#Run model
Y = oakley2004.evaluate(param_values,A,M)

#Analysis
fast_i = fast.analyze(problem,Y,print_to_console=True)



#plotting
fig, ax1 = plt.subplots(1,1, figsize=(12,6))
ax1 = barplot(fast_i.to_df(), ax=ax1)
ax1.set_xlabel("Inputs")
ax1.set_ylabel("SA indices")
plt.show()
