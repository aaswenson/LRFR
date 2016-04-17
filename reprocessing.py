## This code processes input dictionaries from the MCNP output files

from output_parse import file_parse
import re
from pyne.material import Material
import parameters

# unpack user parameters

file = open('mcfrout177.txt')

mass_flow = parameters.mass
time_step = parameters.time
fuel_mat  = parameters.fuel
reprocessing_efficiency = 1

mat_dat = file_parse(file)

# unpack data material by class from dictionary
actindes = mat_dat['Actinides']
carrier = mat_dat['Carrier Material']
fission_products = mat_dat['Fission Products']

mass_frac_fp = sum(fission_products.itervalues())  # determine mass fraction of fission products

mass_frac_fuel = mass_frac_fp*reprocessing_efficiency   # convert fps into fertile fuel, taking into account efficency

fuel_dict = {'92238':mass_frac_fuel}    # load fuel 
fp_dict = fission_products*(1-reprocessing_efficiency)

actinides = actinides + fuel_dict                   # update mass fractions for fuel and fission products
fission_products = fission_products + fp_dict

print(actinides)
print(fission_products)
