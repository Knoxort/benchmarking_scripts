# Greg Stitt
# University of Florida

# LIMITATIONS:
# - (Minor) Currently treats 1-element arrays on the actual function as a single variable
# - (Minor) config file can't have any whitespace in the specification of a single item

# TODO: Fix parsing of constants: trailing ] brackets are accepted for some reason
# TODO: Fix problem with primitives with different name than key 
# TODO: Change function specification in config file to support non-float args?
# TODO: common subexpressions in trees (see deap sr example, use x**4 to also
# provide x**3 and x**2
# TODO: Make mutation generic function parameterized again in simplifyMutation
# TODO: Move error checking for missing keys into initGP instead of parse functions
# TODO: Cleanup exception handling
# TODO: Parameterize evaluation function and sample generation

import numpy
import math
import operator
import random
import sys
import inspect
import argparse
import random
import time
import os
from collections import defaultdict

# 3rd party
from deap import base, tools, gp, algorithms, creator

# local
import primitives
import functions
import fitness
import ea
import config
import probability as prb
import program
import log
    

def main():

    # get command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="The configuration file for approximation")
    parser.add_argument("-p", "--plot", 
                        help="Plot results (for 1-input only)",
                        action="store_true")
    args = parser.parse_args()
    configFile = args.config_file
    configName = os.path.splitext(configFile)[0]

    # parse configuration file to get parameter values
    configParameters = config.parseConfigFile(configFile)

    config.parameters.update(configParameters)
    pset = config.parameters[config.PRIMITIVES_KEY]
    
    #Equation to be mapped
    equation = "add(mul(mul(add(mul(alpha, 0.000732227829058), -4.64060202838e-07), add(mul(cube(lx1), mul(mul(add(mul(cube(lx1), 1.01470490879), -82.8196489564), mul(\
lelt, 30.1169841553)), 3.85621280433e-06)), lx1)), 1.00039568689), -0.0106298997359)"

    ind = ea.Individual.from_string(equation, pset)
	     

    # graph the tree
    filename = "hof_tree_out.pdf"
    ind.output_tree(filename)

#    return hof

if __name__ == "__main__":
    hof = main()


