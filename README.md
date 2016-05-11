
# LRFR

Proposal for a MCNP Input/Output File Editor for Steady State Isotope Analysis in Liquid Fueled Reactors

This project will aim to develop a Python script that will take information from MCNP6 output files to write new MCNP6 input files, initiating subsequent runs. It will repeat the process for a given number of intervals. When writing the new input files, the program will be able to edit the number densities of critical isotopes in order to simulate fuel reprocessing for a liquid-fueled reactor. The project should be general enough to work with any geometry, fuel composition, and reprocessing scheme. It will also be robust enough to recognize common errors and output error warnings to simplify debugging for users. Upon completion, this project will be submitted for consideration as an addition to the PyNE framework.

The project will look to some of the existing PyNE tools for MCNP input and output interfacing as an example. Despite some guidance from past works, the project will be an original initiative. It will showcase the group's knowledge of Python. Specifically, the project will focus on Python's interaction with the computer system, as well as Python's ability to search through text files for specific, desired information. This information of course, relevant to changing isotopic compositions in a Liquid Fueled Reactor throughout the burnup process. Outside of Python, the project will demonstrate the goup's understanding of MCNP6.


========================================================================================================================================================================

USING LRFR FOR LIQUID FUELED REACTOR FUEL REPROCESSING

1. This script is dependent on a working installation of MCNP6, ensure that MCNP is on your computer's path before execution
2. There are 5 scripts necessary to run the reprocessing code, they are available on the github repository on branch USER
	- LRFR.py
	- error_checkRevI.py
	- make_new_input.py
	- output_parse.py
	- reprocessing_RevI.py
	- parameters.py
3. The program is executed by calling the module LRFR.py using a python interpreter 
4. Before executing verify:
	- MCNP input file runs with no errors
	- All parameter fields have been filled
		- reprocessing material
		- number of reprocessing intervals (note, it is the user's responsibility to set the length of intervals in the MCNP input file)
		- fuel carrier material 
		- number of cores on which to run MCNP6
		- input and output file names
		
