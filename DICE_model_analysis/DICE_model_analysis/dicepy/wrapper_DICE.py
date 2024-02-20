import numpy as np
from dice_params import DiceParams
from dice_dynamics import simulateDynamics, dumpState
import pandas as pd


def wrapper_dice(ml0, mu0, mat0, fco22x, t2xco2, tocean0, tatm0, k0, dk,
                 num_times,
                 tstep,
                 output_variable):
    '''Important: if you change the inputs: you have to manually modify
    the inputs of the function and also argsv: if something by default is
    ok, place it in argsv as p._NAME (the names are respected)'''


    t = np.arange(1, num_times + 1)

    p = DiceParams(num_times, tstep)
    outputType = 1

    start_year = 2015
    final_year = start_year + p._tstep * num_times
    years = np.linspace(start_year, final_year, num_times, dtype=np.int32)

    argsv = [-1.0, outputType, num_times,
             p._tstep,
             p._al, p._l, p._sigma, p._cumetree, p._forcoth,
             p._cost1, p._etree, p._scale1, p._scale2,
             ml0, mu0, mat0, p._cca0,
             p._a1, p._a2, p._a3,
             p._c1, p._c3, p._c4,
             p._b11, p._b12, p._b21, p._b22, p._b32, p._b23, p._b33,
             fco22x, t2xco2,
             p._rr, p._gama,
             tocean0, tatm0, p._elasmu, p._prstp, p._expcost2,
             k0, dk, p._pbacktime,
             0, 0.0, 0.0]

    args = tuple(argsv)

    scenariosDF = pd.read_csv("./Reference_Objective_Scenarios.csv")
    scenariosDF.columns = ['Sav1', 'Miu1', 'Sav2', 'Miu2', 'Sav3', 'Miu3']

    S_start = scenariosDF['Sav1'].values
    MIU_start = scenariosDF['Miu1'].values

    #    Arbitrary starting values for the control variables:
    #    S_start = np.full(num_times,0.2596)
    #    MIU_start = np.full(num_times,  0.03)
    x_start = np.concatenate([MIU_start, S_start])

    output = simulateDynamics(x_start, *args)

    dumpState(years, output, "./results/scenarioOutput.csv")

    #the output is:
    #              -rows: the time istants (in years)
    #              -cols: the different output variables: only the one of interest is retained
    return output[:,output_variable]








