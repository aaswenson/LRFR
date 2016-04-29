# ------------------- MCNP Error Handling ---------------- #

# This module checks the runs of MCNP for errors, reacts accordingly 

import re

def check_for_missingXS(outfile):
    file = open(outfile)
    errors = []
    f = str('fatal error.   cross-section tables missing for zaid =')
    for line in file:
        if f in line:
            XS = re.findall(r'\d+',line)
            errors.append(XS)
    return errors


def write_omit_number(inputfile,omit_add,error_check_number):  
    with open('inputfile_cp'+error_check_number,'w') as newfile:
        with open(inputfile, 'a+') as file:
            file.seek(0)
            for line in file:
                s = 'omit='
                if line[0] == ' ' and s in line:
                    oldline = line
                    line.split
                    old_num_omit = re.findall(r'\d+',line)
                    old_num_omit = old_num_omit[0]
            
                    omit = str(int(old_num_omit) + omit_add)
            
                    omit = str('omit='+omit)
                    line = oldline.replace('omit='+old_num_omit,omit)
                    newfile.write(line)
                else:
                    newfile.write(line)
        file.close()
    file.close()
    return newfile

# filename = 'interval_0o'
# errors = check_for_missingXS(filename)
# print(errors)

inputfile = 'errorcheck.i'
newfile = write_omit_number(inputfile,24)
print(newfile)