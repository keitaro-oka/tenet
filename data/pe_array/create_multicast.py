num_pe_col=64
num_pe_row=64

##################
# 2D multicast
#################
path_w = '/home/oka/TENET/data/pe_array/oka_own/'+'pe_2dmulticast.p'
with open(path_w, mode='w') as f:
    str_tmp="{PE[i,j]:0<=i<"+str(num_pe_col)+" and 0<=j<"+str(num_pe_col)+"}\n" 
    f.write(str_tmp)
    str_tmp="{"
    for i_index in range(0,48):
        for j_index in range(0,4):
            if i_index == 0 and j_index == 0:
                continue
            i_index_str = "i" + "+" + str(i_index)
            j_index_str = "j" + "+" + str(j_index)
            if i_index == 0:
                i_index_str = "i"
            if j_index == 0:
                j_index_str = "j"
    
            str_tmp=str_tmp+"PE[i,j]->PE["+i_index_str+","+j_index_str+"]"
            if (i_index == 47 and j_index == 47) == False:
                str_tmp=str_tmp+";"
    
    str_tmp=str_tmp+"}"
    f.write(str_tmp)

##################
# 1D multicast (row)
#################

path_w = '/home/oka/TENET/data/pe_array/oka_own/'+'pe_1dmulticast_i.p'
with open(path_w, mode='w') as f:
    str_tmp="{PE[i,j]:0<=i<"+str(num_pe_col)+" and 0<=j<"+str(num_pe_col)+"}\n"
    f.write(str_tmp)
    str_tmp="{"
    for i_index in range(0,48):
    #for i_index in range(-24,24):
        i_index_str = "i" + "+" + str(i_index)
        if i_index == 0:
            continue
    
        str_tmp=str_tmp+"PE[i,j]->PE["+i_index_str+",j]"
        if (i_index == 47) == False:
            str_tmp=str_tmp+";"
    
    str_tmp=str_tmp+"}"
    f.write(str_tmp)

##################
# 1D multicast (col)
#################

path_w = '/home/oka/TENET/data/pe_array/oka_own/'+'pe_1dmulticast_j.p'
with open(path_w, mode='w') as f:
    str_tmp="{PE[i,j]:0<=i<"+str(num_pe_col)+" and 0<=j<"+str(num_pe_col)+"}\n"
    f.write(str_tmp)
    str_tmp="{"
    #for j_index in range(-25,24):
    for j_index in range(0,48):
        j_index_str = "j" + "+" + str(j_index)
        if j_index == 0:
            continue
    
        str_tmp=str_tmp+"PE[i,j]->PE[i,"+j_index_str+"]"
        if (j_index == 47) == False:
            str_tmp=str_tmp+";"
    
    str_tmp=str_tmp+"}"
    f.write(str_tmp)
