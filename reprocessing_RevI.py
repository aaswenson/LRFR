# Import helpful tools
import math

def fraction_stay(par,t):
    f_gone = par.V_dot/par.V*int(t)*par.eta_reprocessing
    f_stay = 1 - f_gone
    return f_stay

def reprocessing(dict_mass, f_stay, mat, sigma_lib = '73c'):
    tot_i = 0
    m_gone = 0
    dict_wf = {mat: {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }}
    for subsubdict in dict_mass[mat]:
        for subsubsubdict in dict_mass[mat][subsubdict]:
            tot_i = tot_i + dict_mass[mat][subsubdict][subsubsubdict]
    for subsubsubdict in dict_mass[mat]['Fission Products']:
        m_gone = m_gone + dict_mass[mat]['Fission Products'][subsubsubdict]*(1-f_stay)
        dict_mass[mat]['Fission Products'][subsubsubdict] = dict_mass[mat]['Fission Products'][subsubsubdict]*f_stay
        wf = dict_mass[mat]['Fission Products'][subsubsubdict]/tot_i
        dict_wf[mat]['Fission Products'][subsubsubdict] = mcnp_line(subsubsubdict, wf, sigma_lib)
    for subsubsubdict in dict_mass[mat]['Actinides']:
        wf = dict_mass[mat]['Actinides'][subsubsubdict]/tot_i
        dict_wf[mat]['Actinides'][subsubsubdict] = mcnp_line(subsubsubdict, wf, sigma_lib)
    for subsubsubdict in dict_mass[mat]['Carrier Material']:
        wf = dict_mass[mat]['Carrier Material'][subsubsubdict]/tot_i
        dict_wf[mat]['Carrier Material'][subsubsubdict] = mcnp_line(subsubsubdict, wf, sigma_lib)
    dict_mass[mat]['Actinides']['92238'] = dict_mass[mat]['Actinides']['92238'] + m_gone
    wf = dict_mass[mat]['Actinides']['92238']/tot_i
    dict_wf[mat]['Actinides']['92238'] = mcnp_line('92238', wf, sigma_lib)
    return dict_mass, dict_wf

def mcnp_line(key, value, sigma_lib = '73c'):
    line = '      ' + str(key) + '.' + str(sigma_lib) + '  -' + str(value)
    return line
