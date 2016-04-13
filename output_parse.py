# Import helpful tools
import re

# Parameters used to improve efficiency

# Import some MCNP output files in order to run some tests
full_file = open('mcfrout177.txt')
act_file = open('mcfr_act_test.txt')


def file_parse(file, dict):
    burn_bool = false
    burn_str = 'burnup summary table by material'
    act_bool = false
    act_str = 'actinide inventory for material'
    fp_bool = false
    fp_str = 'nonactinide inventory for material'
    end_str = 'estimated keff results by cycle'
    for line in file:
        # Added to ignore non-nurnup data and thus decrease computation time
        if burn_str in line:
            burn_bool = True
        elif act_str in line:
            act_bool = True
        elif fp_str in line:
            act_bool = False
            fp_bool = True
        elif end_str in line:
            fp_bool = False
            burn_bool = False
        if burn_bool == True:
            actinides = line_parse(line)


def line_parse(line, dict):
    line = re.sub(r'^.*[a-zA-z][a-zA-z].*$', "", line)
    if line.isspace() == True:
        pass
    else:
        line = line.split()
        ID = line[1]
        mass_frac = line[7]
        dict[ID] = mass_frac
    return dict

#dict = {}
#for line in act_file:
#    line_parse(line, dict)

#print(dict)
        
