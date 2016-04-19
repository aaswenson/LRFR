#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocessing, fraction_stay

# Importinf the problem parameters
from parameters import V, V_dot, mat, eta_reprocessing 

#Importing some useful tools
from nose.tools import assert_equal

#-----------------------------------------#
#Tests of the actinide parsing function

# Run test to verify it will read a basic file
def test_line_basic():
    act_file = open('mcfr_act_test.txt')
    dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
    for line in act_file:
        line_parse(line, dict)
    obs = dict['Actinides']['92235']
    exp = 2.862E-06
    assert_equal(obs, exp)
    act_file.close()

# Run test to verify it will read files with lines that aren't useful
def test_line_comment():
    act_file_comment = open('mcfr_act_test_comment.txt')
    dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
    for line in act_file_comment:
        line_parse(line, dict)
    obs = dict['Actinides']['92238']
    exp = 5.014E-01
    assert_equal(obs, exp)
    act_file_comment.close()

# Run a test to verify the whole output parsing function works for actinides
def test_full_act():
    full_file = open('mcfrout177.txt')
    dict = file_parse(full_file)
    obs = dict[mat]['Actinides']['92238']
    exp = 4.972E-01
    assert_equal(obs, exp)
    full_file.close()

# Run a test to verify the whole output parsing function works for carrier materials
def test_full_car():
    full_file = open('mcfrout177.txt')
    carrier = [11, 17]
    dict = file_parse(full_file, carrier)
    obs = dict[mat]['Carrier Material']['11023']
    exp = 4.762E-02
    assert_equal(obs, exp)
    full_file.close()

# Run a test to verify the whole output parsing function works for fission products
def test_full_FP():
    full_file = open('mcfrout177.txt')
    dict = file_parse(full_file)
    obs = dict[mat]['Fission Products']['54135']
    exp = 5.616E-07
    assert_equal(obs, exp)
    full_file.close()

# Run a test to see that the functions can read the time step taken
def test_dt():
    in_file = open('MCFR177_in.txt')
    obs = time_step(in_file)
    exp = '200'
    assert_equal(obs, exp)
    in_file.close()

# Run a test to make sure the fraction that stays is computed correctly
def test_frac():
    t = 200
    import parameters as par
    obs = fraction_stay(par, t)
    exp = 0.7142857142857143
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works for the simple case of pure U-238
def test_repro_238():
    mat = '1'
    f_stay = 0.5
    act = {'92238':1}
    dict = {mat:{'Actinides':act, 'Carrier Material':{}, 'Fission Products':{} }}
    dict = reprocessing(dict, f_stay, mat)
    obs = dict[mat]['Actinides']['92238']
    exp = 1
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works for a simple case of U-238 and some actinides
def test_repro_FP(): 
    mat = '1'
    f_stay = 0.5
    act = {'92238':0.9}
    fp = {'52135':0.1}
    dict = {mat:{'Actinides':act, 'Carrier Material':{}, 'Fission Products':fp }}
    dict = reprocessing(dict, f_stay, mat)
    obs = dict[mat]['Fission Products']['52135']
    exp = 0.05
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works for a simple case of U-238 and some carrier salt
def test_repro_car(): 
    mat = '1'
    f_stay = 0.5
    act = {'92238':0.9}
    car = {'11023':0.1}
    dict = {mat:{'Actinides':act, 'Carrier Material':car, 'Fission Products':{} }}
    dict = reprocessing(dict, f_stay, mat)
    obs = dict[mat]['Carrier Material']['11023']
    exp = 0.1
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works for a simple case of U-238 and some actinides
def test_repro_act(): 
    mat = '1'
    f_stay = 0.5
    act = {'92238':0.9}
    car = {'11023':0.1}
    dict = {mat:{'Actinides':act, 'Carrier Material':car, 'Fission Products':{} }}
    dict = reprocessing(dict, f_stay, mat)
    obs = dict[mat]['Carrier Material']['11023']
    exp = 0.1
    assert_equal(obs, exp)


