# ------------------- MCNP Error Handling ---------------- #

# This module checks the runs of MCNP for errors, reacts accordingly 

import re
# import fileinput
# import parameters as par

def check_for_missingXS(outfile):
    file = open(outfile)
    errors = []
    f = str('fatal error.   cross-section tables missing for zaid =')
    for line in file:
        if f in line:
            XS = re.findall(r'\b\d+\b',line)
            errors.extend(XS)
        omit_add = len(errors)
    file.close()
    return errors, omit_add

def parse_first_omit_line(infile):
    file = open(infile)
   
    s = 'omit='
    for line in file:
   
        if line[0] == ' ' and s in line:
            first_omitline = line.split()
            remove_index = len(first_omitline)
            old_omit_number = first_omitline[1]
            first_omitline = first_omitline[2:remove_index]
            
            omit_line = ''
            for item in first_omitline:
                omit_line = omit_line + str(item+' ')     
   
    file.close()
    
    return omit_line, old_omit_number

def replace_omit_list(infile,new_infile,errors,omit_add,omit_line,old_omit_number, par):
    oldfile = open(infile,'r')
    newfile = open(new_infile, 'w+')
 
    new_omit_number = omit_add + int(old_omit_number)
   
    omit_first_line = '     omit='+str(par.mat)+' '+str(new_omit_number)+' ' + omit_line + '\n'
 
    for line in oldfile:
        c = 0
           
        if line[0] == ' ' and 'omit=' in line:
            newfile.write(omit_first_line)
            for i in range(0,len(errors)):
                add = '                 '+errors[i]+'\n'
                newfile.write(add)
             #c = 1
            
        elif c == 1:
            pass
            
        elif c == 2:
            pass
        else:
            newfile.write(line)
    oldfile.close()
    newfile.close()
    
    return 
    


