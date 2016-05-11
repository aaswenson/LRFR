

Liquid-fueled Reactor Fuel Reprocessing

This set of scripts performs fuel reprocessing calculations on a model of a liquid fueled nuclear reactor. The script uses the depletion capability of MCNP6 to deplete fuel, pass the material data to python modules, reprocess the fuel and initiate subsequent runs with MCNP6. This script was developed as a final project for a scientific computing course (EP476) in the Engineering Physics department at the University of Wisconsin-Madison. Special thanks to Professor Paul Wilson for his guidance throughout the project.


========================================================================================================================================================================

USING LRFR FOR LIQUID FUELED REACTOR FUEL REPROCESSING

1. This script is dependent on a working installation of MCNP6, ensure that MCNP is on your computer's path before execution
2. There are 6 scripts necessary to run the reprocessing code, they are available on the github repository on branch 'master'
	- LRFR.py
    - run_utilities.py
	- error_checkRevI.py
	- make_new_input.py
	- output_parse.py
	- reprocessing_RevI.py
	- parameters.py
all of these utilities are available under the final_version branch on https://www.github.com/aaswenson/LRFR
ALL 6 FILES MUST BE IN THE WORKING DIRECTORY FOR THE SCRIPT TO RUN
3. The program is executed by calling the module LRFR.py using a python interpreter 
4. Before executing verify:
	- MCNP input file runs with no errors
	- All parameter fields have been filled
		- reprocessing material
		- number of reprocessing intervals (note, it is the user's responsibility to set the length of intervals in the MCNP input file)
		- fuel carrier material 
		- number of cores on which to run MCNP6
		- input and output file names
    - Check to verify that any desired optional parameters have been specified, parameters file contains more details
    

=============================================================================================================================================

TESTING LRFR    

1. ensure the following scripts and files are in your working directory
    - tests.py
    - parameters_for_tests.py
    - mcfr401test.txt
    - mcfr401.txt
    - mcfr_act_test.txt
    - mcfr_act_test_comment.txt
    - mcfrout177.txt
    - MCFR177_in.txt    
    - input_test.i
    - error_handle_test_file.txt
2. run nosetests from the command line 
3. ensure success for all 19 tests
		

=============================================================================================================================================

KNOWN ISSUES

1. Any material created by the depletion utility of MCNP6 will be added to new fuel compositions. If a material that does not have a cross section is created and added to the fuel by the reprocessing code, the next run of error_checkRevI will add that material to the MCNP6 omit card. This will cause a fatal error in MCNP. You cannot omit a material that is in your depletion material. 

2. The code cannot be run twice with out cleaning your repository or respecifying output file names

============================================================================================================================================

NOTES

1. runtpe files from MCNP get very large and disk space can be an issue! While the code is running, runtpe's from completed MCNP intervals can be deleted with CAREFUL DISCRETION!





