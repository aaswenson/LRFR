# This script calls all modules to run the reprocessing scheme
# This script is dependent on mcnp6 


import parameters as par
import sys
import os
import subprocess
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocess, find_fraction_stay, make_input_dict
from make_new_input import rewrite_inp_file
from error_checkRevI import check_for_missingXS, parse_first_omit_line, replace_omit_list

inputFile = par.inputfile
intervals = par.intervals



# function to call MCNP
def mcnp_call(inputfile, name, cores, source = 0):
    run_command = ["mcnp6","i="+inputfile, "n=" + name ,"tasks "+cores]
    if source != 0:
        run_command.append("srctp=" + source)
    subprocess.call(run_command)

def material_write(dict,interval,state):
    target = open('burn_data.txt','a')
    if state == 0:
        state = 'Pre'
    else: 
        state = 'Post'
        target.write('# -----------'+state+' Reprocessing Material Data for Burn Interval '+interval+' ---------- #')
    for key in dict:
        isotope_data = str(key) + '      ' + str(dict[key])
        target.write(isotope_data)
    
    
        
# copy original input file for safekeeping
# save_command =["cp",inputFile,"runFile.txt"]
# subprocess.call(save_command)
runFile = inputFile # 'runFile.txt'


for i in range(0,intervals):
    
    # prepare args and call mcnp  
    i = str(i)
    mcnp_name = 'interval_' + i
    t = time_step(inputFile)
    try:
        par.source
        mcnp_call(runFile, mcnp_name, par.cores, par.source)
    except AttributeError:
        print("WARNING: Starting source not specified. Will run without")
        mcnp_call(runFile, mcnp_name, par.cores)
    full_file_name = mcnp_name + 'o'
    full_file = open(full_file_name)
    error_bool = False
    for line in full_file:
        if 'fatal error.   cross-section tables missing for zaid =' in line:
            error_bool = True
            break
    full_file.close()
    if error_bool == True:
        errors,omit_add = check_for_missingXS(full_file_name)
        omit_line, old_omit_number = parse_first_omit_line(runFile)
        new_file = 'interval_' + i + '_new'
        replace_omit_list(runFile,new_file,errors,omit_add,omit_line,old_omit_number, par)
        new_file_name = new_file + 'results'
        try: 
            par.source
            mcnp_call(new_file, new_file_name, par.cores, par.source)
        except AttributeError:
            print("WARNING: Starting source not specified. Will run without")
            mcnp_call(new_file, new_file_name, par.cores)
        full_file_name = new_file_name + 'o'
    out_file = open(full_file_name)
    try:
        par.carrier
        dict = file_parse(out_file, par.carrier)
    except AttributeError:
        print("WARNING: Carrier material not specified. Will be ignored")
        dict = file_parse(out_file)
    out_file.close()
    # write pre reprocessing data to text file
    material_write(dict,i,0)    

    # reprocess
    f_stay = find_fraction_stay(par,t)
    try:
        par.makeup_iso
        dict_mass = reprocess(dict, f_stay, par.mat, par.makeup_iso)
    except AttributeError:
        print("WARNING: Makeup isotopes not specified. Default is 100% U-238")
        dict_mass = reprocess(dict, f_stay, par.mat)
    try:
        par.sigma_lib
        dict_wf = make_input_dict(dict_mass, par.mat, par.sigma_lib)
    except AttributeError:
        print("WARNING: Cross-section library for reprocessed material not specified. Default is 73c")
        dict_wf = make_input_dict(dict_mass, par.mat)
    # write reprocessed data to text file
    material_write(dict_mass,i,1)

    # call input write function
    rewrite_inp_file(inputFile,dict_wf,par.mat)
    
    

        
    














