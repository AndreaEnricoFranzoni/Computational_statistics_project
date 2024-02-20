import wrapper_DICE
import numpy as np



def evaluation_model(inputs,
                     output_variable,
                     num_times = 50,
                     tstep = 1.0,
                     final_istant = 14):
    '''
    Does the evaluation of the DICE model wrt the sampling that has been made
    Parameters
    ----------
    inputs: sampling points: it is a matrix N x k
    output_variable: 1 for emissions, 2 for C02PPM, 6 for Consumption Per Capita
    num_times: how many time steps I have to evaluate
    tstep: how long the time steps (in years) (with this default values, I'll evaluate every year for 50 years starting from 2015
            (actually the first evaluation is done on 2016))
    final_istant: the year for which I am interested on the output: default: 2030 (with that num_times and tstep)

    Returns: array containing the output
    -------
    '''

    N = inputs.shape[0]
    output = np.zeros(N)

    #inputs names: ml0, mu0, mat0, fco22x, t2xco2, tocean0, tatmo0, k0, dk
    '''
    If you want to change inputs: you have to modify here the number
    of inputs, and possibly their name in order to avoid confusion.
    Also, in the for cicle you have to pass the correct in put in the correct
    order
    '''
    ml0 = inputs[:,0]
    mu0 = inputs[:,1]
    mat0 = inputs[:,2]
    fco22x = inputs[:,3]
    t2xco2 = inputs[:,4]
    tocean0 = inputs[:,5]
    tatm0 = inputs[:,6]
    k0 = inputs[:,7]
    dk = inputs[:,8]

    for i in range(N):
        output[i] = wrapper_DICE.wrapper_dice(ml0[i], mu0[i], mat0[i], fco22x[i], t2xco2[i],
                                              tocean0[i], tatm0[i], k0[i], dk[i],
                                              num_times,tstep,output_variable)[final_istant]

    return output



