#===============================================================================
# Function to take copy of old input file and add in new material compositions
#===============================================================================

def update_inp_mats(input_file_cp, reprocess_dict, mat_num):
    # Make new mcnp input material string
    new_mat = []
    for subsubdict in reprocess_dict[mat_num]:
        for subsubsubdict in reprocess_dict[mat_num][subsubdict]:
            mat_line = reprocess_dict[mat_num][subsubdict][subsubsubdict]
            new_mat.append(mat_line)

    # Now loop through file, record input file before and after old material
    orig_before = []
    orig_after = []
    with open(input_file_cp, 'r+') as inp_file:

        # Loop through beginning of file up to material that needs to be updated
        mat_num_len = len(mat_num)+1
        mat_num_str = 'm'+str(mat_num)+' '
        for line in inp_file:
            if line[0:1+mat_num_len] == mat_num_str:
                print('I found the material to be changed')
                break
            else:
                orig_before.append(line)

        # Loop through rest of old material definition and ignore it
        for line in inp_file:
            if line[0:5] == '     ':
                pass
            else:
                orig_after.append(line)
                break

        # Loop through and save every line of rest of file
        for line in inp_file:
            orig_after.append(line)

        print(orig_after)
        # Now rewrite file with new material in place of old fuel material
        inp_file.seek(0)
        inp_file.truncate()
        for i in range(len(orig_before)):
            inp_file.write(orig_before[i])

        new_mat_line_one = 'm' + mat_num + new_mat[0]
        inp_file.write(new_mat_line_one)

        for i in range(1,len(new_mat)):
            inp_file.write(new_mat[i])

        for i in range(len(orig_after)):
            inp_file.write(orig_after[i])

    return 

        
