#===============================================================================
# Functions to take copy of old input file and add in new material compositions
#===============================================================================

def make_new_mat(reprocess_dict, mat_num):
    # Make new mcnp input material string
    new_mat = []
    for subsubdict in reprocess_dict[mat_num]:
        for subsubsubdict in reprocess_dict[mat_num][subsubdict]:
            mat_line = reprocess_dict[mat_num][subsubdict][subsubsubdict]
            new_mat.append(mat_line)

    new_mat_line_one = 'm' + mat_num + new_mat[0]
    new_mat[0] = new_mat_line_one

    return new_mat

def save_old_file_lines(inp_file_cp, mat_num):
    # Now loop through file, record input file before and after old material
    orig_before = []
    orig_after = []
    with open(input_file_cp, 'r') as inp_file:
        # Loop through beginning of file up to material that needs to be updated
        mat_num_len = len(mat_num)+1
        mat_num_str = 'm'+str(mat_num)+' '
        for line in inp_file:

            if line[0:1+mat_num_len] == mat_num_str:
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

    return orig_before, orig_after


def rewrite_inp_file(new_inp_file, reprocess_dict, mat_num):

    # Call for lines to write to file
    new_lines = make_new_mat(reprocess_dict, mat_num)
    old_file_begin, old_file_end = save_old_file_lines(new_inp_file)
       
    # Open file
    with open(new_inp_file, 'w+') as inp_file:

        # Now rewrite file with new material in place of old fuel material
        inp_file.seek(0)
        #inp_file.truncate()
        for i in range(len(old_file_begin)):
            inp_file.write(old_file_begin[i])

        for i in range(1,len(new_mat)):
            inp_file.write(new_mat[i])

        for i in range(len(old_file_end)):
            inp_file.write(old_file_end[i])

    return 

        
