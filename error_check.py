# ------------------- MCNP Error Handling ---------------- #

# This module checks the runs of MCNP for errors, reacts accordingly 

import re

def error_check(outfile,interval):
    file = open(outfile+interval)
    errors = []
    f = str('fata')
    for line in file:
        if f in line:
            errors.append(line)
    return errors

errors = error_check('out','q')
print(errors)
