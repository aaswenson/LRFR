# This script calls all modules to run the reprocessing scheme
# This script is dependent on mcnp6 


import parameters as par
#, intervals, cores
import os
import subprocess
from output_parse import line_parse, file_parse
from input_parse import time_step
from reprocessing_RevI import reprocessing, fraction_stay, trunc_sig_fig, trunc_large_number 
from make_new_input import update_inp_mats

inputFile = par.inputfile
intervals = par.intervals
args = [par.cores]


def mcnp_call(inputfile,args,i):
    arg = args[0]
    run_command = ["mcnp6","i="+inputFile,"n=interval_"+ i , "tasks "+arg]
    subprocess.call(run_command)
 
# copy original input file for safekeeping
save_command =["cp",inputFile,"runFile.txt"]
subprocess.call(save_command)
runFile = 'runFile.txt'

for i in range(0,intervals):
    i = str(i)

    t = time_step(inputFile)

    mcnp_call(runFile,args,i)
  
    full_file = open('interval_'+i+'o')
    dict = file_parse(full_file, par.carrier)
    print(dict)
    f_stay = fraction_stay(par,t)
    dict_mass, dict_wf = reprocessing(dict, f_stay, par.mat, par.sigma_lib)

    # call input write function
    update_inp_mats(inputFile,dict_wf,par.mat)
    
    

        
    














