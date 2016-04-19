#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from input_parse import time_step
from reprocessing_RevI import reprocessing

# Importinf the problem parameters
from parameters import V, V_dot, mat, eta_reprocessing 

#Importing some useful tools
from nose.tools import assert_equal

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
act_file = open('mcfr_act_test.txt')
act_file_comment = open('mcfr_act_test_comment.txt')

#-----------------------------------------#
#Tests of the actinide parsing function

# Run test to verify it will read a basic file
def test_line_basic():
    dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
    for line in act_file:
        line_parse(line, dict)
    obs = dict['Actinides']['92235']
    exp = 2.862E-06
    assert_equal(obs, exp)

# Run test to verify it will read files with lines that aren't useful
def test_line_comment():
    dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
    for line in act_file_comment:
        line_parse(line, dict)
    obs = dict['Actinides']['92238']
    exp = 5.014E-01
    assert_equal(obs, exp)

def test_full():
    dict = file_parse(full_file)
    obs = dict[mat]['Actinides']['92238']
    exp = 4.972E-01
    assert_equal(obs, exp)
