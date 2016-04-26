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
 
  
for i in range(0,intervals):
    i = str(i)

    t = time_step(inputFile)

    mcnp_call(inputFile,args,i)
  
    full_file = open('interval_'+i+'o')
    dict = file_parse(full_file, par.carrier)
    f_stay = fraction_stay(par,t)
    dict_mass, dict_wf = reprocessing(dict, f_stay, par.mat, par.sigma_lib)

    # call input write function
    update_inp_mats(inputFile,dict_wf,par.mat)
    
    
    
# this loop will roll through the burnup interval, running MCNP and saving outputs along the way
    #inputFile = inputmakerdohicky(inputfile)

        
    




# Begin pseudo code for loopz and such
# import input file
# grab time step from intervals





# Things this programs should do
# ls the directory, pass it in and look for existing MCNP output files
    # if they are there, throw exception, warning of potential data loss






# THINGS AN INPUT WRITER SHOULD DO

# change the burn card so the user can define different intervals (higher BOC fidelity) 
# change materials (obviously)

