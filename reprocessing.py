# This code takes an mcnp output file and performs a fuel reprocessing scheme

from pyne.material import Material
import numpy as np
import re
from input import parameters

material = [] # intialize list for materials
file=open('mcfrout177.txt')

# this function parses the mcnp output file to look for materials
# materials are stored in a list for further processing

for line in file:
     if [0-9][0-9][0-9][0-9][0-9] in line:
          material = line
for 

# begin fuel reprocessing
# replace fission product volume with fuel

cumulative_fp_conc = numpy.cumsum(material)
volume_fp = parameters.volume*cumulative_fp_conc

# find mass of fission products and henceforth, fuel
mass_fuel = parameters.fueldensity*volume_fp

