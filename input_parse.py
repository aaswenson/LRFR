# Import helpful tools
import re

# Function to parse whole files into just post-burnup weight percentages
def time_step(file_name):
    file = open(file_name)
    time_str = 'burn time='
    time = 0
    while time == 0:
        line = file.readline()
        if time_str in line:
            line_1 = line.strip(time_str)
            line_1 = line_1.split()
            time = line_1[0]
    file.close()
    return time
        
