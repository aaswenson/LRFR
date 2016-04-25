#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocessing, fraction_stay
from make_new_input import update_inp_mats

# Importing the problem parameters
import parameters as par

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
in_file = open('MCFR177_in.txt')

dict = file_parse(full_file, par.carrier)


t = time_step(in_file)

f_stay = fraction_stay(par,t)

print(f_stay)
print(par.V_dot)
print(par.mat)
print(type(par.mat))

dict_mass, dict_wf = reprocessing(dict, f_stay, par.mat, par.sigma_lib)

print(dict_wf[par.mat]['Carrier Material'])
full_file.close()
in_file.close()

# Now test if the new input function works
orig_before, orig_after, new_mat_line_one = update_inp_mats('MCFR177_in_new_mats.txt', dict_wf, par.mat)
