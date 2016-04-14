# Import helpful tools
import re

# Parameters used to improve efficiency

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
act_file = open('mcfr_act_test.txt')

carrier = [11, 17]
def file_parse(file, carrier = []):
    dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
    burn_bool = False
    start_str = 'burnup summary table by material'
    end_str = 'estimated keff results by cycle'
    for line in file:
        # Added to ignore non-nurnup data and thus decrease computation time
        if start_str in line:
            burn_bool = True
        elif end_str in line:
            burn_bool = False
        if burn_bool == True:
            dict = line_parse(line, dict, carrier)
    return dict


def line_parse(line, dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }, carrier = []):
    line = re.sub(r'^.*[a-zA-z][a-zA-z].*$', "", line)
    if line.isspace() == True:
        pass
    else:
        line = line.split()
        if len(line) == 8:
            ID = line[1]
            mass_frac = line[7]
            z = int(int(ID)/1000)
            if z >= 90:
                dict['Actinides'][ID] = mass_frac
            elif z in carrier:
                dict['Carrier Material'][ID] = mass_frac
            else: 
                dict['Fission Products'][ID] = mass_frac
    return dict

full_file = open('mcfrout177.txt')
dict = file_parse(full_file)
print(dict)
        
