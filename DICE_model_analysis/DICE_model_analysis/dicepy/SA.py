import numpy as np
import matplotlib.pyplot as plt
from SALib.sample import latin
from SALib.analyze import delta
from SALib.plotting.bar import plot as barplot
import random
from evaluation_model import evaluation_model

SEED = 230300
np.random.seed(SEED)
random.seed(SEED)

n_samples = 1000

#time istants are by default: 50 years from 2015, 1 year of time step, stop at 2030

#output variable: taken from this list
out = 2
#for further explanations: https://whynot.readthedocs.io/en/latest/simulator_configs/dice.html
names_response = [
    'Industrial emissions CO2',                                         #0
    'Emissions CO2',                                                    #1
    'C02PPM',                                                           #2
    'Temperature of atmosphere',                                        #3
    'Gross world product net of abatement and damages',                 #4
    'Damages as fraction of gross output',                              #5
    'Per capita consumption thousands US dollars',                      #6
    'Carbon price',                                                     #7
    'Emission control rate optimal',                                    #8
    'Real interest rate per annum',                                     #9
    'SOCCC',                                                            #10
    'll',                                                               #11
    'Level of total factor productivity',                               #12
    'Gross world product Gross of abatement and damages',               #13
    'Capital stock trillions US dollars',                               #14
    'Gross savings rate as fraction of gross world product optimal',    #15
    'Investment trillions US dollars',                                  #16
    'Output net damages equation',                                      #17
    'Cumulative industrial carbon emissions',                           #18
    'Total industrial carbon emissions',                                #19
    'Carbon concentration in lower oceans',                             #20
    'Carbon concentration in shallow oceans',                           #21
    'Radiative forcing (watts per m2)',                                 #22
    'Temperature of lower oceans (°C)',                                 #23
    'Damages (trillions USD)',                                          #24
    'Cost of emissions reductions',                                     #25
    'Marginal cost of abatement',                                       #26
    'Consumption (trillions USD)',                                      #27
    'One period utility function',                                      #28
    'Period utility',                                                   #29
    'Carbon concentration in atmosphere'                                #30
]




#inputs names
inputs = [ 'x1',                      #ML0:        Initial concentration in lower strata
           'x2',                      #MU0:        Initial concentration in upper strata
           'x3',                      #MAT0:       Initial concentration in atmosphere
           'x4',                      #FCO22X:     Forcings of equilibrium CO2 doubling
           'x5',                      #T2XCO2:     Equilibrium temperature impact
           'x6',                      #TOCEAN0:    Initial lower stratum temperature change
           'x7',                      #TATM0:      Initial atmospheric temperature change
           'x8',                      #K0:         Initial capital value
           'x9'                       #DK:         Depreciation rate on capital
           ]
N = len(inputs)

#problem definition according to SALib
#the distributions of the paramters are assumed being normal:
#for mean the value of DIcePy has been taken, while for the variance the choice
#has been done based on some Internet data
problem={
    'num_vars': N,
    'names': inputs,
    'bounds': [
            [1740, 20],
            [460,5],
            [851,8],
            [3.8,0.1],
            [3.0,0.1],
            [0.82,0.01],
            [0.0068,0.0001],
            [220,15],
            [0.5,0.2]

        ],
    'dists': ["norm",
              "norm",
              "norm",
              "norm",
              "norm",
              "norm",
              "norm",
              "norm",
              "triang"
              ],
}

#sampling (LHS)
param_values = latin.sample(problem,n_samples,)

#output evaluation
Y = evaluation_model(param_values,output_variable=out)

#delta coefficients
delta_i = delta.analyze(problem,param_values,Y,
                    print_to_console=True)


delta_indices = delta_i.to_df()[['delta','delta_conf']]

#plotting
fig, ax1 = plt.subplots(1,1, figsize=(12,6))
ax1 = barplot(delta_indices, ax=ax1)
ax1.set_xlabel("Inputs")
ax1.set_ylabel("Delta value")

ax1.set_title(f'Output: {names_response[out]}')
plt.show()
