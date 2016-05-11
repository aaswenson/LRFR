# function to call MCNP

def mcnp_call(inputfile, name, cores, source = 0):
    run_command = ["mcnp6","i="+inputfile, "n=" + name ,"tasks "+cores]
    if source != 0:
        run_command.append("srctp=" + source)
    subprocess.call(run_command)

# optional function to output reprocessing data
def material_write(dict,interval,state):
    target = open('burn_data.txt','a')
    if state == 0:
        state = 'Pre'
    else: 
        state = 'Post'
        target.write('# -----------'+state+' Reprocessing Material Data for Burn Interval '+interval+' ---------- #')
    for key in dict:
        isotope_data = str(key) + '      ' + str(dict[key])
        target.write(isotope_data)
