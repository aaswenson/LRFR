# This script calls all modules to run the reprocessing scheme
# This script is dependent on mcnp6 


from parameters import inputfile
import os
import subprocess

inputFile = inputfile

commandList = ["mcnp6","i="+inputFile, "tasks 16"]

subprocess.run(commandList)

