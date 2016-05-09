#====================================================================
# Nose Tests to make sure functions that are rewriting the input
#               files are working properly
#====================================================================

# import functions
from make_new_input import make_new_mat, save_old_file_lines, rewrite_inp_file
from nose.tools import assert_equal 

# testing functions
def test_make_new_mat():
    dict_wf = {'4': {'Actinides': {'92234': '      92234.73c  -3.352e-06\n', \
                                   '92235': '      92235.73c  -4.532e-06\n'}, \
                     'Carrier Material': {'11023': '      11023.73c   -7.2543e-03\n', \
                                          '17035': '      17035.73c   -4.3624e-03\n'}, \
                     'Fission Products': {'12024': '      12024.73c   -5.2333e-11\n', \
                                          '14029': '      14029.73c   -6.4333e-10\n'}}}
    obs = make_new_mat(dict_wf, '4')
    exp = ['m4      92234.73c  -3.352e-06\n', '      92235.73c  -4.532e-06\n', \
           '      11023.73c   -7.2543e-03\n', '      17035.73c   -4.3624e-03\n' \
           '      12024.73c   -5.2333e-11\n', '      14029.73c   -6.4333e-10\n']
    assert_equal(obs,exp)


