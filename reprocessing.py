## This code processes input dictionaries from the MCNP output files

from out_parse import file_parse
import re
from pyne.material import Materials
import parameters

# unpack user parameters

file = open('outp')

mass_flow = parameters.mass
time_step = parameters.time
fuel_mat  = parameters.fuel

mat_dat = file_parse(file)

# unpack data material by class from dictionary
actindes = mat_dat['Actinides']
carrier = mat_dat['Carrier Material']
fission_products = mat_dat['Fission Products']

mass_frac_fp = sum(fission_products.itervalues())


