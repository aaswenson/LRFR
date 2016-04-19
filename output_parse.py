# Import helpful tools
import re

# Function to parse whole files into just post-burnup weight percentages
def file_parse(file, carrier = []):
    mat = 0
    dict = {}
    sub_dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
    burn_bool = False
    start_str = 'burnup summary table by material'
    end_str = 'estimated keff results by cycle'
    mat_str = 'actinide inventory for material'
    for line in file:
        # Added to ignore non-nurnup data and thus decrease computation time
        if start_str in line:
            burn_bool = True
        elif end_str in line:
            burn_bool = False
        if mat_str in line:
            line_1 = line.split()
            mat_1 = line_1[4]
            if mat == 0:
                mat = mat_1
            elif mat == mat_1:  
                pass
            else:
                print('im here')
                dict[mat] = sub_dict
                mat = mat_1
                sub_dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }
        if burn_bool == True:
            sub_dict = line_parse(line, sub_dict, carrier)
    dict[mat] = sub_dict
    return dict

# Function to parse individual lines into post-burnup weight percentages
def line_parse(line, sub_dict = {'Actinides':{}, 'Carrier Material':{}, 'Fission Products':{} }, carrier = []):
    line = re.sub(r'^.*[a-zA-z][a-zA-z].*$', "", line)
    if line.isspace() == True:
        pass
    else:
        line = line.split()
        if len(line) == 8:
            ID = line[1]
            mass_frac = float(line[7])
            z = int(int(ID)/1000)
            if z >= 90:
                sub_dict['Actinides'][ID] = mass_frac
            elif z in carrier:
                sub_dict['Carrier Material'][ID] = mass_frac
            else: 
                sub_dict['Fission Products'][ID] = mass_frac
    return sub_dict
        
