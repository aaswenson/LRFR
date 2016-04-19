#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocessing, fraction_stay

# Importinf the problem parameters
from parameters import V, V_dot, mat, eta_reprocessing 

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
act_file = open('mcfr_act_test.txt')
in_file = open('MCFR177_in.txt')


carrier = [11, 17]
dict = file_parse(full_file, carrier)
#print(dict)

t = time_step(in_file)
#print(' ')
#print(t)

f_gone = V_dot/V*int(t)*eta_reprocessing
f_stay = 1 - f_gone

print(f_stay)
print(V_dot)

dict = reprocessing(dict, f_stay, mat)

#print(dict)

full_file.close()
act_file.close()
act_file_comment.close()
