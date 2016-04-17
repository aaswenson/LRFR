# Import helpful tools
import math

def reprocessing(dict, f_stay, mat):
    tot = 0
    for subsubsubdict in dict[mat]['Fission Products']:
        dict[mat]['Fission Products'][subsubsubdict] = dict[mat]['Fission Products'][subsubsubdict]*f_stay
    for subsubsubdict in dict[mat]['Fission Products']:
        tot = tot + dict[mat]['Fission Products'][subsubsubdict]
    for subsubsubdict in dict[mat]['Actinides']:
        tot = tot + dict[mat]['Actinides'][subsubsubdict]
    for subsubsubdict in dict[mat]['Carrier Material']:
        tot = tot + dict[mat]['Carrier Material'][subsubsubdict]
    dict[mat]['Actinides']['92238'] = dict[mat]['Actinides']['92238'] + 1 - tot
    print(tot)
    return dict
