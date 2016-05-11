#====================================================================
# Nose Tests to make sure functions that are rewriting the input
#               files are working properly
#====================================================================

# import functions
from make_new_input import make_new_mat, save_old_file, rewrite_inp_file
from nose.tools import assert_equal 

# testing functions
def test_make_new_mat():
    dict_wf = {'4': {'Actinides': {'92234': '      92234.73c  -3.352e-06\n', \
                                   '92235': '      92235.73c  -4.532e-06\n'}, \
                     'Carrier Material': {'11023': '      11023.73c   -7.2543e-03\n', \
                                          '17035': '      17035.73c   -4.3624e-03\n'},\
                     'Fission Products': {'12024': '      12024.73c   -5.2333e-11\n', \
                                          '14029': '      14029.73c   -6.4333e-10\n'}}}
    obs = make_new_mat(dict_wf, '4')
    exp = ['m4      92235.73c  -4.532e-06\n', '      92234.73c  -3.352e-06\n', \
           '      12024.73c   -5.2333e-11\n', '      14029.73c   -6.4333e-10\n', \
           '      17035.73c   -4.3624e-03\n', '      11023.73c   -7.2543e-03\n' ]
    assert_equal(obs,exp)


def test_save_old_file():
    inp_file = 'input_test.i'
    mat_num = '1'
    obs_before, obs_after = save_old_file(inp_file, mat_num)
    exp_before = ['-*-mcnpgen-*- -------Table Set Immitation----------\n', 
                  'c Cell Cards\n',
                  '100  1  -0.64  -1:-2:-3:-4:-5:-6:-7    IMP:n=1 $ U=2	 $ Table\n',
                  '\n',
                  'c Surface Cards\n',
                  '1  RPP  -60 60  -60 60  -5 0	 $ Table \n',
                  '\n',
                  'c Material Cards \n']
    exp_after = ['m3   8016    -0.539562\n',
                 '     11023    -0.028191\n',
                 '     13027   -0.011644\n',
                 '     14000   -0.377220\n',
                 '     19000   -0.003321 $ PYREX Borosilcate Glass rho=2.23 g/cc\n',
                 'c \n',
                 'TR1    0 0 0']
    print(obs_after)
    print(exp_after)
    assert_equal(obs_before, exp_before)
    assert_equal(obs_after, exp_after)

