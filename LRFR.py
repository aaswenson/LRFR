# This script calls all modules to run the reprocessing scheme
# This script is dependent on mcnp6 


from parameters import inputfile 
#, intervals, cores
import os
import subprocess
import reprocessing_RevI
import input_parse
import output_parse

inputFile = inputfile
intervals = 2
cores = '4'
args = [cores]


def mcnp_call(inputfile,args,i):
    arg = args[0]
    i = 'i'
    run_command = ["mcnp6","i="+inputFile,"o=interval"+ i , "tasks "+arg]
    subprocess.run(run_command)

for i in range(0,intervals):
    mcnp_call(inputFile,args,i)
    subprocess.run(["ls"])
    

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

