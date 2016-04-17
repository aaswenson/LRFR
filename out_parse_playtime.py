#Importing the functions
from output_parse import line_parse, file_parse

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
act_file = open('mcfr_act_test.txt')


carrier = [11, 17]
dict = file_parse(full_file, carrier)
print(dict)

