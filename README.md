# Computational_statistics_project
The repo contains three folders: one devoted to the analysis of some SALib techniques on a test function, one devoted to the exploitation of the delta method, one devoted to the analysis of the DICE model (2016) through delta method.
Link and references:
- SALib to perform SA: https://github.com/SALib/SALib
- Oakley-O'Hagan test function(2004): https://jeremy-oakley.sites.sheffield.ac.uk
- DicePy to go through DICE model: https://github.com/domokane/DicePy

Folders (all of them can be used after having installed SALib):
-Oakley_Hagan_test: contains simple scripts that exploits the use of SALib to perform SA on the Oakley-O'Hagan test function(2004). Every script can be run independently. Morris method cannot be applied due to the curse of dimensionality (a lot of NaN retrieved);
-delta_analytical_cases: contains simple classes and script to apply the delta method to some particular cases in which the result is known, in order to analyse the SALib's implementation of delta method. Every subfolder contains a specific model, and can be run independently. There are some issues with lognormal inputs for high dimensions;
-DICE_model_analysis: firstly, run installing_dice.py in order to have DicePy. The original repo is completely retained. The idea is to apply delta method at the DICE model to see the effect of a specific output.
The shape of SA.py is the same of every SALib script. The output is chosen (you can modify it in the script: default is C02PPM (2)), and it is evaluated in a specific time (in years) istant: default: 2030. evaluation_model.py recalls DicePy in order to evaluate the output, through a wrapper.
9 inputs are chosen (respectively: Initial concentration in lower strata(x1), Initial concentration in upper strata(x2), Initial concentration in atmosphere(x3), Forcings of equilibrium CO2 doubling(x4), Equilibrium temperature impact(x5), Initial lower stratum temperature change(x6), Initial atmospheric temperature change(x7), Initial capital value(x8), Depreciation rate on capital(x9)), and some assumptions about their distribution is done (primarly gaussian hp). Notice that if you want to change these inputs, you have to manually modify evaluation_model.py and wrapper_DICE.py, as said in the scripts. They seem to be the most reasonable ones. There is a big number of total inputs, and the others have some default values.
Important discaimer: it is possible that this analysis is not good for some output and yet not feasible for some others, due to the dynamics of the model: it strictly dependes on the output chosen.
