#Importing the functions
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocess, find_fraction_stay, mcnp_line, make_input_dict

# Importinf the problem parameters
from parameters import V, V_dot, mat, eta_reprocessing, sigma_lib

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
    exp = 1.182E+02
    assert_equal(obs, exp)
    act_file.close()

# Run test to verify it will read files with lines that aren't useful
def test_line_comment():
    act_file_comment = open('mcfr_act_test_comment.txt')
    dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
    for line in act_file_comment:
        line_parse(line, dict)
    obs = dict['Actinides']['92238']
    exp = 2.071E+07
    assert_equal(obs, exp)
    act_file_comment.close()

# Run a test to verify the whole output parsing function works for actinides
def test_full_act():
    full_file = open('mcfrout177.txt')
    dict = file_parse(full_file)
    obs = dict[mat]['Actinides']['92238']
    exp = 2.051E+07
    assert_equal(obs, exp)
    full_file.close()

# Run a test to verify the whole output parsing function works for carrier materials
def test_full_car():
    full_file = open('mcfrout177.txt')
    carrier = [11, 17]
    dict = file_parse(full_file, carrier)
    obs = dict[mat]['Carrier Material']['11023']
    exp = 1.965E+06
    assert_equal(obs, exp)
    full_file.close()

# Run a test to verify the whole output parsing function works for fission products
def test_full_FP():
    full_file = open('mcfrout177.txt')
    dict = file_parse(full_file)
    obs = dict[mat]['Fission Products']['54135']
    exp = 2.317E+01
    assert_equal(obs, exp)
    full_file.close()

#-----------------------------------------#
#Tests of the function that finds the time step

# Run a test to see that the functions can read the time step taken
def test_dt():
    in_file = 'MCFR177_in.txt'
    obs = time_step(in_file)
    exp = '200'
    assert_equal(obs, exp)

#-----------------------------------------#
#Tests of the function that does reprocessing

# Run a test to make sure the fraction that stays is computed correctly
def test_frac():
    t = 200
    import parameters as par
    obs = find_fraction_stay(par, t)
    exp = 0.7142857142857143
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works for the simple case of pure U-238
def test_repro_238():
    sigma_lib = '73c'
    mat = '1'
    f_stay = 0.5
    act = {'92238':100.0}
    dict_mass = {mat:{'Actinides':act, 'Carrier Material':{}, 'Fission Products':{} }}
    dict_mass= reprocess(dict_mass, f_stay, mat)
    obs = dict_mass[mat]['Actinides']['92238']
    exp = 100
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works for a simple case of U-238 and some actinides
def test_repro_FP(): 
    sigma_lib = '73c'
    mat = '1'
    f_stay = 0.5
    act = {'92238':99.0}
    fp = {'52135':1.0}
    dict_mass = {mat:{'Actinides':act, 'Carrier Material':{}, 'Fission Products':fp }}
    dict_mass= reprocess(dict_mass, f_stay, mat)
    obs = dict_mass[mat]['Fission Products']['52135']
    exp = 0.5
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works for a simple case of U-238 and some carrier salt
def test_repro_car(): 
    sigma_lib = '73c'
    mat = '1'
    f_stay = 0.5
    act = {'92238':1.9e6}
    car = {'11023':1.0e5}
    dict_mass = {mat:{'Actinides':act, 'Carrier Material':car, 'Fission Products':{} }}
    dict_mass = reprocess(dict_mass, f_stay, mat)
    obs = dict_mass[mat]['Carrier Material']['11023']
    exp = 1.0e5
    assert_equal(obs, exp)

# Run a test to make sure the reprocessing works when all three categories are present
def test_repro_act(): 
    sigma_lib = '73c'
    mat = '1'
    f_stay = 0.5
    act = {'92238':140.0, '94239':30.0}
    car = {'11023':15.0}
    fp = {'52135':15.0}
    dict_mass = {mat:{'Actinides':act, 'Carrier Material':car, 'Fission Products':fp }}
    dict_mass= reprocess(dict_mass, f_stay, mat)
    obs1 = dict_mass[mat]['Actinides']['94239']
    exp1 = 30.0
    obs2 = dict_mass[mat]['Actinides']['92238']
    exp2 = 147.5
    assert_equal(obs1, exp1)
    assert_equal(obs2, exp2)

# Run a test to see how the reprocessing works with a full file
def test_repro_full_file():
    sigma_lib = '73c'
    full_file = open('mcfrout177.txt')
    f_stay = 0.5
    mat = '4'
    carrier = [11, 17]
    dict_mass = file_parse(full_file, carrier) 
    dict_mass= reprocess(dict_mass, f_stay, mat)
    obs = dict_mass[mat]['Carrier Material']['17035']
    exp = 2.078E+06
    assert_equal(obs, exp)
    full_file.close()


