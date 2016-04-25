#===============================================================================
# Function to take copy of old input file and add in new material compositions
#===============================================================================
import re


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
        for line in inp_file:
            if line[0:2] == 'm'+ mat_num:
                print('I found the material to be changed')
                break
            else:
                orig_before.append(line)
        
        for line in inp_file:
            if line[0] == ' ':
                pass
            else:
                orig_after.append(line)
                break
        for line in inp_file:
            orig_after.append(line)

        # Now rewrite file with new material in place of old fuel material
        inp_file.seek(0)
        for i in range(len(orig_before)):
            inp_file.write(orig_before[i])

        new_mat_line_one = 'm' + mat_num + new_mat[0]
        inp_file.write(new_mat_line_one)

        for i in range(1,len(new_mat)):
            inp_file.write(new_mat[i])

        for i in range(len(orig_after)):
            inp_file.write(orig_after[i])
        
        inp_file.flush()

    return orig_before, orig_after, new_mat_line_one
                

        
