#===============================================================================
# Functions to take copy of old input file and add in new material compositions
#===============================================================================

def update_inp_mats(input_file_cp, reprocess_dict, param):
    # Make new mcnp input material string
    new_mat = []
    for subsubdict in reprocess_dict:
        for subsubsubdict in reprocess_dict[param.mat][subsubdict]:
            mat_line = reprocess_dict[param.mat][subsubdict][subsubsubdict]+'\n'
            new_mat.append(mat_line)

    # Now loop through file, record input file before and after old material
    orig_before = []
    orig_after = []
    with open('input_file_cp', 'r+') as inp_file:
        for line in inp_file:
            row = inp_file.readline()
            row_split = row.split()
            if row_split[0] == 'm'+str(param.mat):
                break
            else:
                orig_before.append(row)
        
        for line in inp_file:
            if line[0] == ' ':
                pass
            else:
                orig_after.append(line)
                break
        
        orig_after.append(inp_file.readlines())

        # Now rewrite file with new material in place of old fuel material
        for i in range(len(orig_before)):
            inp_file.write(orig_before[i])
        
        for i in range(len(new_mat)):
            inp_file.write(new_mat[i])

        for i in range(len(orig_after)):
            inp_file.write(orig_after[i])
        
    


                

        
