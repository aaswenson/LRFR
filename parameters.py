# Total Core Volume [m^3]
V = 28

# Reprocessing rate [L/day]
V_dot = float(40)
# Converting to [m^3/day]
V_dot = V_dot/1000

# Material to do reprocessing in
mat = '100'

# Reprocessing Efficiency 
eta_reprocessing = 1


# Define Input File Name
inputfile = 'test3.txt'


# Cross section library of choice
sigma_lib = '73c'


# Carrier Material
carrier = [11,17]

intervals = 4

cores = '4'

