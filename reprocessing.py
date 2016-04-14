## This code processes input dictionaries from the MCNP output files

from out_parse import file_parse
import re
from pyne.material import Materials
import parameters

# unpack dictionary and convert to PyNE materials

mass_flow = parameters.mass
time_step = parameters.time
fuel_mat  = parameters.fuel


