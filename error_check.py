# ------------------- MCNP Error Handling ---------------- #

# This module checks the runs of MCNP for errors, reacts accordingly 

import re
import fileinput

def check_for_missingXS(outfile):
    file = open(outfile)
    errors = []
    f = str('fatal error.   cross-section tables missing for zaid =')
    for line in file:
        if f in line:
            XS = re.findall(r'\b\d+\b',line)
            errors.extend(XS)
            omit_add = len(errors)
    return errors, omit_add


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

def add_missing_isotopes(inputfile_cp,inputfile_name,errors):
    file_old = open(inputfile_cp,'r')
    file_new = open(inputfile_name,'w')
    s = 'omit='
    for line in file_old:
        file_new.write(line)
        if line[0:4] == ' ' and s in line:
            for i in range(len(errors)):
                omitted_isotope = errors[i]
                file_new.write("omitted_isotope\n")
    file_old.close()
    file_new.close()
    
           
          
        
                
            

  
            
            
            

# filename = 'interval_0o'
# errors = check_for_missingXS(filename)
# print(errors)

#inputfile = 'errorcheck.i'
#newfile = write_omit_number(inputfile,24,'1')
#print(newfile)

errors , omit_add = check_for_missingXS('interval_0o')
print(errors)
write_omit_number('errorcheck.i',omit_add,'1')
add_missing_isotopes('inputfile_cp1','errorcheck.i',errors)








