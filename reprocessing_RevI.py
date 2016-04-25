# Import helpful tools
import math

def fraction_stay(par,t):
    f_gone = par.V_dot/par.V*int(t)*par.eta_reprocessing
    f_stay = 1 - f_gone
    return f_stay

def reprocessing(dict_mass, f_stay, mat, sigma_lib = '73c'):
    tot_i = 0
    m_gone = 0
    trunc_precision = 4
    dict_wf = {mat: {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }}
    for subsubdict in dict_mass[mat]:
        for subsubsubdict in dict_mass[mat][subsubdict]:
            tot_i = tot_i + dict_mass[mat][subsubdict][subsubsubdict]
    for subsubsubdict in dict_mass[mat]['Fission Products']:
        m_gone = m_gone + dict_mass[mat]['Fission Products'][subsubsubdict]*(1-f_stay)
        dict_mass[mat]['Fission Products'][subsubsubdict] = dict_mass[mat]['Fission Products'][subsubsubdict]*f_stay
        wf = dict_mass[mat]['Fission Products'][subsubsubdict]/tot_i
        wf = trunc_sig_fig(wf, trunc_precision)
        dict_wf[mat]['Fission Products'][subsubsubdict] = mcnp_line(subsubsubdict, wf, sigma_lib)
    for subsubsubdict in dict_mass[mat]['Actinides']:
        wf = dict_mass[mat]['Actinides'][subsubsubdict]/tot_i
        wf = trunc_sig_fig(wf, trunc_precision)
        dict_wf[mat]['Actinides'][subsubsubdict] = mcnp_line(subsubsubdict, wf, sigma_lib)
    for subsubsubdict in dict_mass[mat]['Carrier Material']:
        wf = dict_mass[mat]['Carrier Material'][subsubsubdict]/tot_i
        wf = trunc_sig_fig(wf, trunc_precision)
        dict_wf[mat]['Carrier Material'][subsubsubdict] = mcnp_line(subsubsubdict, wf, sigma_lib)
    dict_mass[mat]['Actinides']['92238'] = dict_mass[mat]['Actinides']['92238'] + m_gone
    wf = dict_mass[mat]['Actinides']['92238']/tot_i
    wf = trunc_sig_fig(wf, trunc_precision)
    dict_wf[mat]['Actinides']['92238'] = mcnp_line('92238', wf, sigma_lib)
    return dict_mass, dict_wf

def mcnp_line(key, value, sigma_lib = '73c'):
    line = '      ' + str(key) + '.' + str(sigma_lib) + '  -' + str(value)+'\n'
    return line

def trunc_sig_fig(value, num_sig_fig):
    value = str(value)
    left_of_decimal, right_of_decimal = value.split('.')
    if len(left_of_decimal) + len(right_of_decimal) <= num_sig_fig: 
        value_new = float(value)
    elif 'e' in right_of_decimal:
        number, log_power = right_of_decimal.split('e')
        value_new = left_of_decimal + '.' + number[0:num_sig_fig-1] + 'e' + log_power
        value_new = float(value_new)
    elif right_of_decimal == '0':
        sig_fig = len(left_of_decimal)
        diff_sig_fig = int(sig_fig) - int(num_sig_fig)
        str_0 = ''
        for x in range(0, diff_sig_fig):
            str_0 = str_0 + '0'
        value_new = trunc_large_number(left_of_decimal, num_sig_fig)
        value_new = float(value_new)
    elif left_of_decimal == '0' and right_of_decimal[0] == '0':
        sig_fig_i = len(right_of_decimal)
        without_zero = right_of_decimal.strip('0')
        zero_sig_fig = sig_fig_i - len(without_zero)
        str_0 = ''
        for x in range(0, zero_sig_fig):
            str_0 = str_0 + '0'
        value_new = '0.' + str_0 + without_zero[0:num_sig_fig]
        value_new = float(value_new)
    elif left_of_decimal == '0' and right_of_decimal[0] != '0':
        value_new = '0.' + right_of_decimal[0:num_sig_fig]
        value_new = float(value_new)
    else:
        sig_fig_left = len(left_of_decimal)
        sig_fig_right = len(right_of_decimal)
        if sig_fig_left >= num_sig_fig:
            value_new = trunc_large_number(left_of_decimal, num_sig_fig)
            value_new = float(value_new)
        else:
            diff_sig_fig = int(sig_fig_left) - int(num_sig_fig)
            value_new = left_of_decimal + '.' + right_of_decimal[0:diff_sig_fig]
            value_new = float(value_new)
    return(value_new)

def trunc_large_number(left_of_decimal, num_sig_fig):
    sig_fig = len(left_of_decimal)
    diff_sig_fig = int(sig_fig) - int(num_sig_fig)
    str_0 = ''
    for x in range(0, diff_sig_fig):
        str_0 = str_0 + '0'
    value_new = left_of_decimal[0:num_sig_fig] + str_0 + '.0'
    return value_new













