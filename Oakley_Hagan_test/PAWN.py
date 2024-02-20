import numpy as np
import matplotlib.pyplot as plt
from SALib.sample import latin
from SALib.analyze import pawn
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
pawn_i = pawn.analyze(problem,param_values,Y,print_to_console=True)
#for the Kolmogorov-Smirnov statistic:
#min
#mean
#median
#max
#coefficient of variation (CV) (standard deviation / mean), it indicates the level of variability across the slides, with values closer to zero indicating lower variation.

#plotting
fig, ax1 = plt.subplots(1,1, figsize=(12,6))
ax1 = barplot(pawn_i.to_df(), ax=ax1)
ax1.set_xlabel("Inputs")
ax1.set_ylabel("KS statistic")
plt.show()