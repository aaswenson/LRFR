#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocessing, fraction_stay

# Importinf the problem parameters
import parameters as par

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
in_file = 'MCFR177_in.txt'#open('MCFR177_in.txt')

dict = file_parse(full_file, par.carrier)


t = time_step(in_file)

f_stay = fraction_stay(par,t)

print(f_stay)
print(par.V_dot)

dict_mass, dict_wf = reprocessing(dict, f_stay, par.mat, par.sigma_lib)


