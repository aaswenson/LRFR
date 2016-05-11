# Total Core Volume [m^3]
# Must be a float or integer
V = 28

# Reprocessing rate [L/day]
# Must be a float
V_dot = float(40)
# Converting to [m^3/day]
V_dot = V_dot/1000

# Material to do reprocessing in
# Must be a string
mat = '100'

# Reprocessing Efficiency 
# Must be an integer or float
eta_reprocessing = 1.0

# Define Input File Name
# Must be a string of the file name
inputfile = 'test4.txt'

# Cross section library of choice (Optional, Default is '73c')
# Must be a string
# If not including, comment out the variable
sigma_lib = '73c'


# Carrier Material (Optional, Default is no carrier material)
# Must be a list of integers of the z number
# If not including, comment out the variable
carrier = [11,17]

# Number of time intervals
# Must be an integer
intervals = 2

# Number of cores run on 
# Must be a string
cores = '4'

# Starting source tape (Optional, Default to none, input file MUST be consistent)
# Must be a string of the file name
# If not including, comment out the variable
source = 'srctp'

# Materials to add when removing fission products (Optional. Default is 100% '92238')
# Must be a dictionary taking the form {isotope_id:weight_fraction_of_makeup, ...)
# Isotope Id must be a string taking the form of z*1000+A, weight fraction of the makeup must be a float, with all summing to 1
# If not including, comment out the variable
makeup_iso = {'92238':0.95, '93237':0.002373563312, '94238':0.001057712891, '94239':0.02410049337, '94240':0.01110166638, '94241':0.004550685884, '94242':0.003221419489, '95241':0.002599673593, '95242':0.000005049246848, '95243':0.0007503765027, '96244':0.0002189119749, '96245':0.00002044736327}
