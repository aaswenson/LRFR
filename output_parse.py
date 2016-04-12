import re

file = open('mcfrout177.tx')
bool = false
s = str('burnup summary table by material')

for line in file:
    if s in line:
        bool=true
    if bool == true:
        actinides = act_parse(line)


def act_parse(line):
    line = line.split()
    if line[0] == [0-9]:
        ID = line[1]
        mass_frac = line[7]
# here define the dictionary to store actinide information
        
