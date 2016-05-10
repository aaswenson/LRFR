#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocess, find_fraction_stay, make_input_dict
from make_new_input import rewrite_inp_file

# Importing the problem parameters
import parameters as par

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout401.txt')
in_file = 'mcfr401.txt'

dict = file_parse(full_file, par.carrier)


t = time_step(in_file)

f_stay = find_fraction_stay(par,t)

print(f_stay)
print(par.V_dot)
print(par.mat)
print(type(par.mat))

dict_mass = reprocess(dict, f_stay, par.mat)
dict_wf = make_input_dict(dict_mass, par.mat, par.sigma_lib)

print(dict_wf[par.mat]['Carrier Material'])
full_file.close()

# Now test if the new input function works
rewrite_inp_file('mcfr401_cp.txt', dict_wf, par.mat)
