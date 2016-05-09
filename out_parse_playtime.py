#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import find_fraction_stay, make_input_dict, reprocess

# Importinf the problem parameters
import parameters as par

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
in_file = 'MCFR177_in.txt'


dict = file_parse(full_file, par.carrier)


t = time_step(in_file)

f_stay = find_fraction_stay(par,t)

print(f_stay)
print(par.V_dot)

dict_mass = reprocess(dict, f_stay, par.mat)
dict_input = make_input_dict(dict_mass, par.mat, par.sigma_lib)


