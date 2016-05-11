# Import helpful tools
import math

# Function to find the fraction of Fission Products that will be reprocessed out during the time step
def find_fraction_stay(par,t):
    f_gone = par.V_dot/par.V*int(t)*par.eta_reprocessing
    f_stay = 1 - f_gone
    return f_stay

# Function to a dictionary of MCNP inputs for the material
def make_input_dict(dict_mass, mat, sigma_lib = '73c', dict_input = {}):
    tot_i = 0 
    dict_input[mat] = {}
    for category in dict_mass[mat]:
        dict_input[mat][category] = {}
        for isotope_id in dict_mass[mat][category]:
            tot_i = tot_i + dict_mass[mat][category][isotope_id]
    for category in dict_mass[mat]:
        for isotope_id in dict_mass[mat][category]:
            wf = dict_mass[mat][category][isotope_id]/tot_i
            
            # This was to fix an error of reading -0 as 0, and thus getting mixed weight fraction and atomic fraction error in MCNP
            if wf != 0:
                dict_input[mat][category][isotope_id] = mcnp_line(isotope_id, wf, sigma_lib)

            
    return dict_input


# Function to model reprocessing of fission products during the time step
def reprocess(dict_mass, f_stay, mat, makeup_iso = {'92238':1.0}):
    m_gone = 0
    for isotope_id in dict_mass[mat]['Fission Products']:
        m_gone = m_gone + dict_mass[mat]['Fission Products'][isotope_id]*(1-f_stay)
        dict_mass[mat]['Fission Products'][isotope_id] = dict_mass[mat]['Fission Products'][isotope_id]*f_stay
    for isotope_id in makeup_iso:
        dict_mass[mat]['Actinides'][isotope_id] = dict_mass[mat]['Actinides'][isotope_id] + m_gone*makeup_iso[isotope_id]
    return dict_mass


# Function to write lines that MCNP can read
def mcnp_line(key, value, sigma_lib = '73c'):
    line = '      ' + str(key) + '.' + str(sigma_lib) + '  -' + str(value) + '\n'
    return line














