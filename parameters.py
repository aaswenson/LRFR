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
inputfile = 'test5.txt'


# Cross section library of choice
sigma_lib = '73c'


# Carrier Material
carrier = [11,17]

# Number of time intervals
intervals = 20

# Number of cores run on 
cores = '24'

# Starting source tape 
source = 'srctp'

# Materials to add when removing fission products
makeup_iso = {'92238':0.95, '93237':0.002373563312, '94238':0.001057712891, '94239':0.02410049337, '94240':0.01110166638, '94241':0.004550685884, '94242':0.003221419489, '95241':0.002599673593, '95242':0.000005049246848, '95243':0.0007503765027, '96244':0.0002189119749, '96245':0.00002044736327}
