# Import helpful tools
import math

def find_fraction_stay(par,t):
    f_gone = par.V_dot/par.V*int(t)*par.eta_reprocessing
    f_stay = 1 - f_gone
    return f_stay


def make_input_dict(dict_mass, mat, sigma_lib = '73c', dict_input = {}):
    tot_i = 0 
    dict_input[mat] = {}
    for category in dict_mass[mat]:
        for isotope_id in dict_mass[mat][category]:
            tot_i = tot_i + dict_mass[mat][category][isotope_id]
    for category in dict_mass[mat]:
        for isotope_id in dict_mass[mat][category]:
            wf = dict_mass[mat][category][isotope_id]/tot_i
            if wf == 0:
                wf = 1.0e-11
            dict_input[mat][isotope_id] = mcnp_line(isotope_id, wf, sigma_lib)
    return dict_input

def reprocess(dict_mass, f_stay, mat):
    m_gone = 0
    for isotope_id in dict_mass[mat]['Fission Products']:
        m_gone = m_gone + dict_mass[mat]['Fission Products'][isotope_id]*(1-f_stay)
        dict_mass[mat]['Fission Products'][isotope_id] = dict_mass[mat]['Fission Products'][isotope_id]*f_stay
    dict_mass[mat]['Actinides']['92238'] = dict_mass[mat]['Actinides']['92238'] + m_gone
    return dict_mass

def mcnp_line(key, value, sigma_lib = '73c'):
    line = '      ' + str(key) + '.' + str(sigma_lib) + '  -' + str(value) + '\n'
    return line














