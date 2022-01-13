import itertools

r_size=3
s_size=3
file_id=1


space_num_val_3= [("rx", "ry", "c"), ("rx", "ry", "k")]
space_num_val_4= [("rx", "ry", "ox", "oy"), ("rx", "ry", "c", "k")]
space_num_val_5= [("rx", "ry", "ox", "oy", "c"), ("rx", "ry", "ox", "oy", "k")]
space_num_val_6= [("rx", "ry", "ox", "oy", "c", "k")]

def write_file(str_tmp1, str_tmp2):
    global file_id
    filepath_prefix = '/home/oka/TENET/data/mapping/oka_own/map_data/map_file'
    filepath = filepath_prefix + str(file_id)
    with open(filepath, mode='w') as f:
        f.write(str_tmp1)
        f.write('\n')
        f.write(str_tmp2)
    file_id = file_id + 1

def get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc):
    val_num_t = 4
    str_tmp_l = []
    # rx and ry is always space dim
    #print("get_tmp_str")
    for i in range(1,val_num_t+1):
        comb_l=list(itertools.combinations(["k","ox","oy","c"], i))
        for comb_obj in comb_l:
            j=0
            str_tmp = ""
            print("hogehoge")
            print("val1_alloc", val1_alloc, "val2_alloc", val2_alloc, "val3_alloc", val3_alloc, "val4_alloc", val4_alloc, "val5_alloc", val5_alloc, "val6_alloc", val6_alloc)
            print("comb_obj", comb_obj)
            all_dim = ["n", "k", "c", "ox", "oy"]
            for val in comb_obj:
                if val == val1:
                    str_tmp=str_tmp+"floor("+val+"/"+str(val1_alloc)+")"
                    print("match1")
                elif val == val2:
                    str_tmp=str_tmp+"floor("+val+"/"+str(val2_alloc)+")"
                    print("match2")
                elif val == val3:
                    str_tmp=str_tmp+"floor("+val+"/"+str(val3_alloc)+")"
                    print("match3")
                elif val == val4:
                    str_tmp=str_tmp+"floor("+val+"/"+str(val4_alloc)+")"
                    print("match4")
                elif val == val5:
                    str_tmp=str_tmp+"floor("+val+"/"+str(val5_alloc)+")"
                    print("match5")
                elif val == val6:
                    str_tmp=str_tmp+"floor("+val+"/"+str(val6_alloc)+")"
                    print("match6")
                else:
                    str_tmp=str_tmp+val

                if j < (i-1):
                    str_tmp = str_tmp + "+"

                j=j+1

                all_dim.remove(val)

            tmp_all_dim = all_dim

            str_tmp2 = ""
            for val in tmp_all_dim:
                if val == val1:
                    str_tmp2=str_tmp2+"floor("+val+"/"+str(val1_alloc)+")"
                    print("match1")
                elif val == val2:
                    str_tmp2=str_tmp2+"floor("+val+"/"+str(val2_alloc)+")"
                    print("match2")
                elif val == val3:
                    str_tmp2=str_tmp2+"floor("+val+"/"+str(val3_alloc)+")"
                    print("match3")
                elif val == val4:
                    str_tmp2=str_tmp2+"floor("+val+"/"+str(val4_alloc)+")"
                    print("match4")
                elif val == val5:
                    str_tmp2=str_tmp2+"floor("+val+"/"+str(val5_alloc)+")"
                    print("match5")
                elif val == val6:
                    str_tmp2=str_tmp2+"floor("+val+"/"+str(val6_alloc)+")"
                    print("match6")
                else:
                    str_tmp2=str_tmp2+val

                str_tmp2 = str_tmp2 + ","

            prefix="{S[n,k,c,ox,oy,rx,ry]->T["
            suffix="]}"
            str_tmp = prefix+str_tmp2+str_tmp+suffix
            print(str_tmp)
            str_tmp_l.append(str_tmp)
    print("tmp_dic size")
    print(len(str_tmp_l))
    return str_tmp_l

def process_space_val3(val1, val2, val3,val1_alloc, val2_alloc, val3_alloc, val1_flag, val1_flag, val3_flag):
    if val3_flag == True:
        val_tuple_l = [(val1,val1_alloc),(val2, val2_alloc)]
        val_permu_l = list(itertools.permutations(val_tuple_l))
        
        for val_permu in val_permu_l:
            val1_tmp = val_permu[0][0]
            val2_tmp = val_permu[1][0]
            val1_alloc = val_permu[0][1]
            val2_alloc = val_permu[1][1]
            str_space = get_space_str(3,val1_alloc,val2_alloc,val3_alloc)
            str_tmp_l = get_tmp_str(val1, val2, val3, "ng", "ng", "ng", val1_alloc, val2_alloc, val3_alloc, 0, 0, 0)
            
            if (val1_alloc + val2_alloc) != 32:
                print("error2")
                print("val1", val1_alloc, "val2", val2_alloc)
        
            for str_tmp in str_tmp_l:
                write_file(str_space, str_tmp)
    else:
        str_space = get_space_str(3,val1_alloc,val2_alloc,val3_alloc)
        for str_tmp in str_tmp_l:
            write_file(str_space, str_tmp)

# print 
def get_space_str(dim_num, val1_alloc=0, val2_alloc=0, val3_alloc=0, val4_alloc=0, val5_alloc=0, val6_alloc=0):
    print("get_space_str")
    # num val = 3
    prefix="{S[n,k,c,ox,oy,rx,ry]->PE["
    suffix="]}"
    space_str_list = []

    if dim_num == 3:
        val_tuple_l = [(val1,val1_alloc),(val2, val2_alloc)]
        val_permu_l = list(itertools.permutations(val_tuple_l))

        space_str=val1+"%"+str(val1_alloc)+"+"+val2+"%"+str(val2_alloc)
        space_str=space_str+","+val3+"%"+str(val3_alloc)
        space_str = prefix+space_str+suffix
        space_str_list.append(space_str)

    if dim_num == 4:
        val_tuple_l1 = [(val1,val1_alloc),(val2, val2_alloc)]
        val_permu_l1 = list(itertools.permutations(val_tuple_l))
        val_tuple_l2 = [(val3,val3_alloc),(val4, val4_alloc)]
        val_permu_l2 = list(itertools.permutations(val_tuple_l))

        for val_permu_l1 in val_permu_l1:
            val1_tmp = val_permu[0][0]
            val2_tmp = val_permu[1][0]
            for val_permu_l2 in val_permu_l2:
                val1_alloc_tmp = val_permu[0][1]
                val2_alloc_tmp = val_permu[1][1]

 

        space_str=val1+"%"+str(val1_alloc)+"+"+val2+"%"+str(val2_alloc)
        space_str=space_str+","+val3+"%"+str(val3_alloc)+"+"+val4+"%"+str(val4_alloc)
        space_str_tmp = prefix+space_str+suffix
    if dim_num == 5:
        space_str=val1+"%"+str(val1_alloc)+"+"+val2+"%"+str(val2_alloc)+"+"+val3+"%"+str(val3_alloc)
        space_str=space_str+","+val4+"%"+str(val4_alloc)+"+"+val5+"%"+str(val5_alloc)
        space_str_tmp = prefix+space_str+suffix
    if dim_num == 6:
        space_str=val1+"%"+str(val1_alloc)+"+"+val2+"%"+str(val2_alloc)+val3+"%"+str(val3_alloc)
        space_str=space_str+","+val4+"%"+str(val4_alloc)+"+"+val5+"%"+str(val5_alloc)+val6+"%"+str(val6_alloc)
        space_str_tmp = prefix+space_str+suffix
    print(space_str_tmp)
    return space_str_tmp

print("num val = 3")
space_num=0
space_num2 = 0
for val_list in space_num_val_3:
    dim_sel_hist=[]
    print(val_list)
    print("------")
    dim_sel_l=list(itertools.combinations(val_list,2))
    print(dim_sel_l) 
    for dim_sel_obj in dim_sel_l:
        if set(dim_sel_obj) in dim_sel_hist:
            print("continue")
            continue
        space_num2 = space_num2 + 1
        print("dim_sel_obj", dim_sel_obj)
        print("dim_sel_hist", dim_sel_hist)
        comb_diff = tuple(set(val_list).difference(set(dim_sel_obj)))
        dim_sel_hist.append(set(comb_diff))
        dim_sel_hist.append(set(dim_sel_obj))
        print("comb_diff",comb_diff) 
        space_str=""
        val1, val2 = dim_sel_obj
        val3, *val4 = comb_diff
        print("dim_sel_hist")
        print(dim_sel_hist)
        num_pe_col=32
        num_pe_row=32
        val1_flag=False
        val2_flag=False
        val3_flag=False

        if ("rx" == val1) or ("ry" == val1):
            val1_flag=True
        if ("rx" == val2) or ("ry" == val2):
            val2_flag=True
        if ("rx" == val3) or ("ry" == val3):
            val3_flag=True

        print("val1_flag", "val2_flag", "val3_flag")
        print(val1_flag, val2_flag, val3_flag)
        print(val1, val2, val3)

        if (val1_flag == False) and (val2_flag == True) and (val3_flag == True):
            space_num = space_num + 1
            val1_alloc = num_pe_row-r_size
            val2_alloc=r_size
            val3_alloc = r_size
            str_space = get_space_str(3,val1_alloc,val2_alloc,val3_alloc)
            if ((val1_alloc + val2_alloc) != 32):
                print("error1")
                print("val1", val1_alloc, "val2", val2_alloc)
            str_tmp_l = get_tmp_str(val1, val2, val3, "ng", "ng", "ng", val1_alloc, val2_alloc, val3_alloc, 0, 0, 0)
            for str_tmp in str_tmp_l:
                write_file(str_space, str_tmp)

        if (val1_flag == True) and (val2_flag == False) and (val3_flag == True):
            space_num = space_num + 1
            val1_alloc=r_size
            val2_alloc = num_pe_row-r_size
            val3_alloc = r_size

        if (val1_flag == True) and (val2_flag == True) and (val3_flag == False):
            space_num = space_num + 1
            val1_alloc=r_size
            val2_alloc=r_size
            val3_alloc = num_pe_row
            str_space = get_space_str(3,val1_alloc,val2_alloc,val3_alloc)
            str_tmp_l = get_tmp_str(val1, val2, val3, "ng", "ng", "ng", val1_alloc, val2_alloc, val3_alloc, 0, 0, 0)
            for str_tmp in str_tmp_l:
                write_file(str_space, str_tmp)
print("space_num", space_num)
print("space_num2", space_num2)

print("num val = 4")
space_num=0
space_num2=0
space_num3=0
for val_list in space_num_val_4:
    dim_sel_hist=[]
    print(val_list)
    print("------")
    dim_sel_l=list(itertools.combinations(val_list,2))
    print(dim_sel_l) 
    for dim_sel_obj in dim_sel_l:
        if set(dim_sel_obj) in dim_sel_hist:
            print("continue")
            continue
        space_num2 = space_num2 + 1
        print(dim_sel_obj) 
        comb_diff = tuple(set(val_list).difference(set(dim_sel_obj)))
        dim_sel_hist.append(set(comb_diff))
        dim_sel_hist.append(set(dim_sel_obj))
        print("comb_diff",comb_diff) 
        space_str=""
        val1, val2 = dim_sel_obj
        val3, val4 = comb_diff
        num_pe_col=32
        num_pe_row=32
        val1_flag=False
        val2_flag=False
        val3_flag=False
        val4_flag=False
        print("val1", "val2", "val3", "val4")
        print(val1, val2, val3, val4)

        if ("rx" == val1) or ("ry" == val1):
            val1_flag=True
        if ("rx" == val2) or ("ry" == val2):
            val2_flag=True
        if ("rx" == val3) or ("ry" == val3):
            val3_flag=True
        if ("rx" == val4) or ("ry" == val4):
            val4_flag=True
        print("val1_flag", "val2_flag", "val3_flag", "val4_flag")
        print(val1_flag, val2_flag, val3_flag, val4_flag)

        if (val1_flag == True) and (val2_flag == True) and (val3_flag == False) and (val4_flag == False):
            space_num=space_num+1
            val1_alloc = r_size
            val2_alloc = r_size
            val3_val4_comb_l=list(itertools.combinations(range(1,num_pe_row),1))
            for val3_val4_comb in val3_val4_comb_l:
                val3_alloc,*_ = val3_val4_comb
                val4_alloc = num_pe_row - val3_alloc
                str_space = get_space_str(4,val1_alloc,val2_alloc,val3_alloc,val4_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, "ng", "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, 0, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

            if (val3_alloc + val4_alloc) != 32:
                print("error3")
                print("val3", val3_alloc, "val4", val4_alloc)

        if (val1_flag == True) and (val2_flag == False) and (val3_flag == True) and (val4_flag == False):
            space_num=space_num+1
            val1_alloc = r_size
            val2_alloc = num_pe_row-r_size
            val3_alloc = r_size
            val4_alloc = num_pe_row-r_size
            str_space = get_space_str(4,val1_alloc,val2_alloc,val3_alloc,val4_alloc)
            str_tmp_l = get_tmp_str(val1, val2, val3, val4, "ng", "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, 0, 0)
            space_num3=space_num3+1
            for str_tmp in str_tmp_l:
               write_file(str_space, str_tmp)

            if (val1_alloc + val2_alloc) != 32:
                print("error4")
                print("val1", val1_alloc, "val2", val2_alloc)

            if (val3_alloc + val4_alloc) != 32:
                print("error5")
                print("val3", val3_alloc, "val4", val4_alloc)


        if (val1_flag == True) and (val2_flag == False) and (val3_flag == False) and (val4_flag == True):
            space_num=space_num+1
            val1_alloc = r_size
            val2_alloc = num_pe_row - r_size
            val3_alloc = num_pe_row - r_size
            val4_alloc = r_size
            str_space = get_space_str(4,val1_alloc,val2_alloc,val3_alloc,val4_alloc)
            str_tmp_l = get_tmp_str(val1, val2, val3, val4, "ng", "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, 0, 0)
            space_num3=space_num3+1
            for str_tmp in str_tmp_l:
               write_file(str_space, str_tmp)

            if (val1_alloc + val2_alloc) != 32:
                print("error6")
                print("val1", val1_alloc, "val2", val2_alloc)

            if (val3_alloc + val4_alloc) != 32:
                print("error7")
                print("val3", val3_alloc, "val4", val4_alloc)


print("space_num", space_num)
print("space_num2", space_num2)
print("space_num3", space_num3)

print("num val = 5")
space_num=0
space_num2=0
space_num3=0

for val_list in space_num_val_5:
    dim_sel_hist=[]
    print(val_list)
    print("------")
    dim_sel_l=list(itertools.combinations(val_list,3))
    print(dim_sel_l) 
    for dim_sel_obj in dim_sel_l:
        if set(dim_sel_obj) in dim_sel_hist:
            print("continue")
            continue
        space_num2=space_num2+1
        print(dim_sel_obj) 
        comb_diff = tuple(set(val_list).difference(set(dim_sel_obj)))
        dim_sel_hist.append(set(comb_diff))
        dim_sel_hist.append(set(dim_sel_obj))
        print("comb_diff",comb_diff) 
        space_str=""
        val1, val2, val3 = dim_sel_obj
        val4, val5 = comb_diff

        num_pe_col=32
        num_pe_row=32
        val1_flag=False
        val2_flag=False
        val3_flag=False
        val4_flag=False
        val5_flag=False
        print("val1", "val2", "val3", "val4", "val")
        print(val1, val2, val3, val4)

        if ("rx" == val1) or ("ry" == val1):
            val1_alloc=r_size
            val1_flag=True
        if ("rx" == val2) or ("ry" == val2):
            val2_alloc=r_size
            val2_flag=True
        if ("rx" == val3) or ("ry" == val3):
            val3_alloc=r_size
            val3_flag=True
        if ("rx" == val4) or ("ry" == val4):
            val4_alloc=r_size
            val4_flag=True
        if ("rx" == val5) or ("ry" == val5):
            val5_alloc=r_size
            val5_flag=True

        print("val1_flag", "val2_flag", "val3_flag", "val4_flag", "val5_flag")
        print(val1_flag, val2_flag, val3_flag, val4_flag, val5_flag)

        if (val1_flag == True) and (val2_flag == True) and (val3_flag == False) and (val4_flag == False) and (val5_flag == False):
            space_num=space_num+1
            val1_alloc = r_size
            val2_alloc = r_size
            val3_alloc = num_pe_row - 2*r_size

            val4_val5_comb_l=list(itertools.combinations(range(1,num_pe_row),1))
            for val4_val5_comb in val4_val5_comb_l:
                val4_alloc,*_ = val4_val5_comb
                val5_alloc = num_pe_row - val4_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error8")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error9")
                    print("val4", val4_alloc, "val5", val5_alloc)


        # hoge
        if (val1_flag == True) and (val2_flag == False) and (val3_flag == False) and (val4_flag == True) and (val5_flag == False):
            space_num=space_num+1
            val1_alloc = r_size
            val4_alloc = r_size
            val5_alloc = num_pe_row - r_size
            val2_val3_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val2_val3_comb in val2_val3_comb_l:
                val2_alloc,*_ = val2_val3_comb
                val3_alloc = num_pe_row - r_size - val2_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error10")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error11")
                    print("val4", val4_alloc, "val5", val5_alloc)

        if (val1_flag == True) and (val2_flag == False) and (val3_flag == False) and (val4_flag == False) and (val5_flag == True):
            space_num=space_num+1
            val1_alloc = r_size
            val4_alloc = num_pe_row - r_size
            val5_alloc = r_size
            val2_val3_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val2_val3_comb in val2_val3_comb_l:
                val2_alloc,*_ = val2_val3_comb
                val3_alloc = num_pe_row - r_size - val2_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error12")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error13")
                    print("val4", val4_alloc, "val5", val5_alloc)


        # 1
        if (val1_flag == False) and (val2_flag == True) and (val3_flag == True) and (val4_flag == False) and (val5_flag == False):
            space_num=space_num+1
            val1_alloc = num_pe_row-2*r_size
            val2_alloc = r_size
            val3_alloc = r_size

            val4_val5_comb_l=list(itertools.combinations(range(1,num_pe_row),1))
            for val4_val5_comb in val4_val5_comb_l:
                val4_alloc,*_ = val4_val5_comb
                val5_alloc = num_pe_row - val4_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error14")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error15")
                    print("val4", val4_alloc, "val5", val5_alloc)


        # 2
        if (val1_flag == False) and (val2_flag == True) and (val3_flag == True) and (val4_flag == False) and (val5_flag == False): #2
            space_num=space_num+1
            val1_alloc = num_pe_row-2*r_size
            val2_alloc = r_size
            val3_alloc = r_size
            val4_val5_comb_l=list(itertools.combinations(range(1,num_pe_row),1))
            for val4_val5_comb in val4_val5_comb_l:
                val4_alloc,*_ = val4_val5_comb
                val5_alloc = num_pe_row - val4_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error16")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error17")
                    print("val4", val4_alloc, "val5", val5_alloc)
        
        # 4
        if (val1_flag == False) and (val2_flag == False) and (val3_flag == True) and (val4_flag == False) and (val5_flag == True):
            space_num=space_num+1
            val3_alloc = r_size
            val4_alloc = num_pe_row - r_size
            val5_alloc = r_size
            val1_val2_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val1_val2_comb in val1_val2_comb_l:
                val1_alloc,*_ = val1_val2_comb
                val2_alloc = num_pe_row - val1_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error18")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error19")
                    print("val4", val4_alloc, "val5", val5_alloc)
 
        # 5
        if (val1_flag == False) and (val2_flag == True) and (val3_flag == True) and (val4_flag == False) and (val5_flag == False):
            space_num=space_num+1
            val1_alloc = num_pe_row - r_size
            val2_alloc = r_size
            val3_alloc = r_size
            val4_val5_comb_l=list(itertools.combinations(range(1,num_pe_row),1))
            for val4_val5_comb in val4_val5_comb_l:
                val4_alloc,*_ = val4_val5_comb
                val5_alloc = num_pe_row - val4_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error20")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error21")
                    print("val4", val4_alloc, "val5", val5_alloc)
 
        # 6, 7, 8, 9
        if (val1_flag == False) and (val2_flag == False) and (val3_flag == True) and (val4_flag == False) and (val5_flag == True):
            space_num=space_num+1
            val3_alloc = r_size
            val4_alloc = num_pe_row - r_size
            val5_alloc = r_size

            val1_val2_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val1_val2_comb in val1_val2_comb_l:
                val1_alloc,*_ = val1_val2_comb
                val2_alloc = num_pe_row - val1_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error22")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc) != 32:
                    print("error23")
                    print("val4", val4_alloc, "val5", val5_alloc)
 

        # 10
        if (val1_flag == False) and (val2_flag == False) and (val3_flag == False) and (val4_flag == True) and (val5_flag == True):
            space_num=space_num+1
            val4_alloc = r_size
            val5_alloc = r_size
            val1_val2_val3_comb_l=list(itertools.combinations(range(1,num_pe_row),2))
            for val1_val2_val3_comb in val1_val2_val3_comb_l:
                val1_alloc,val2_alloc,*_ = val1_val2_val3_comb
                val2_alloc = val2_alloc - val1_alloc
                val3_alloc = num_pe_row - val1_alloc - val2_alloc
                str_space = get_space_str(5,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error24")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)



print("space_num", space_num)
print("space_num2", space_num2)
print("space_num3", space_num3)

print("num val = 6")
space_num=0
space_num2=0
space_num3=0
for val_list in space_num_val_6:
    dim_sel_hist=[]
    print(val_list)
    print("------")
    dim_sel_l=list(itertools.combinations(val_list,3))
    print(dim_sel_l) 
    for dim_sel_obj in dim_sel_l:
        if set(dim_sel_obj) in dim_sel_hist:
            print("continue")
            continue
        space_num2=space_num2+1
        print(dim_sel_obj) 
        comb_diff = tuple(set(val_list).difference(set(dim_sel_obj)))
        dim_sel_hist.append(set(comb_diff))
        dim_sel_hist.append(set(dim_sel_obj))
        print("comb_diff",comb_diff) 
        space_str=""
        val1, val2, val3 = dim_sel_obj
        val4, val5, val6 = comb_diff

        val1_flag=False
        val2_flag=False
        val3_flag=False
        val4_flag=False
        val5_flag=False
        val6_flag=False

        if ("rx" == val1) or ("ry" == val1):
            val1_alloc=r_size
            val1_flag=True
        if ("rx" == val2) or ("ry" == val2):
            val2_alloc=r_size
            val2_flag=True
        if ("rx" == val3) or ("ry" == val3):
            val3_alloc=r_size
            val3_flag=True
        if ("rx" == val4) or ("ry" == val4):
            val4_alloc=r_size
            val4_flag=True
        if ("rx" == val5) or ("ry" == val5):
            val5_alloc=r_size
            val5_flag=True
        if ("rx" == val6) or ("ry" == val6):
            val6_alloc=r_size
            val6_flag=True

        print("val1_flag", "val2_flag", "val3_flag", "val4_flag", "val5_flag", "val6_flag")
        print(val1_flag, val2_flag, val3_flag, val4_flag, val5_flag, val6_flag)
        # 1,2
        if (val1_flag == False) and (val2_flag == False) and (val3_flag == False) and (val4_flag == False) and (val5_flag == True) and (val6_flag == True):
            space_num=space_num+1
            val4_alloc = num_pe_row - r_size
            val5_alloc = r_size
            val6_alloc = r_size
            val1_val2_val3_comb_l=list(itertools.combinations(range(1,num_pe_row),2))

            for val1_val2_val3_comb in val1_val2_val3_comb_l:
                val1_alloc,val2_alloc,*_ = val1_val2_val3_comb
                val2_alloc = val2_alloc - val1_alloc
                val3_alloc = num_pe_row - val2_alloc
                str_space = get_space_str(6,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)

                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error26")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc + val6_alloc) != 32:
                    print("error27")
                    print("val4", val4_alloc, "val5", val5_alloc, "val6", val6_alloc)
 

        # 3,4,6,7,8,9
        if (val1_flag == False) and (val2_flag == False) and (val3_flag == True) and (val4_flag == False) and (val5_flag == False) and (val6_flag == True):
            space_num=space_num+1
            val3_alloc = r_size
            val6_alloc = r_size
            val1_val2_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val1_val2_comb in val1_val2_comb_l:
                val1_alloc,*_ = val1_val2_comb
                val2_alloc = num_pe_row - val1_alloc

                val4_val5_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
                for val4_val5_comb in val4_val5_comb_l:
                    val4_alloc,*_ = val4_val5_comb
                    val5_alloc = num_pe_row - val4_alloc

                    str_space = get_space_str(6,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
                    str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)
                    space_num3=space_num3+1
                    for str_tmp in str_tmp_l:
                        write_file(str_space, str_tmp)

                    if (val1_alloc + val2_alloc + val3_alloc) != 32:
                        print("error28")
                        print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                    if (val4_alloc + val5_alloc + val6_alloc) != 32:
                        print("error29")
                        print("val4", val4_alloc, "val5", val5_alloc, "val6", val6_alloc)
 

        # 5,10
        if (val1_flag == False) and (val2_flag == True) and (val3_flag == True) and (val4_flag == False) and (val5_flag == False) and (val6_flag == False):
            space_num=space_num+1
            val1_alloc = num_pe_row - r_size
            val2_alloc = r_size
            val3_alloc = r_size

            val4_val5_val6_comb_l=list(itertools.combinations(range(1,num_pe_row),2))
            for val4_val5_val6_comb in val4_val5_val6_comb_l:
                val4_alloc,val5_alloc,*_ = val4_val5_val6_comb
                val5_alloc = val5_alloc - val4_alloc
                val6_alloc = num_pe_row - val5_alloc
                str_space = get_space_str(6,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error30")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc + val6_alloc) != 32:
                    print("error31")
                    print("val4", val4_alloc, "val5", val5_alloc, "val6", val6_alloc)
 






        # 5,10
        if (val1_flag == True) and (val2_flag == True) and (val3_flag == False) and (val4_flag == False) and (val5_flag == False) and (val6_flag == False):
            space_num=space_num+1
            val1_alloc = r_size
            val2_alloc = r_size
            val3_alloc = num_pe_row - r_size*2

            val4_val5_val6_comb_l=list(itertools.combinations(range(1,num_pe_row),2))
            for val4_val5_val6_comb in val4_val5_val6_comb_l:
                val4_alloc,val5_alloc,*_ = val4_val5_val6_comb
                val6_alloc = num_pe_row - val5_alloc
                val5_alloc = val5_alloc - val4_alloc
                str_space = get_space_str(6,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
                str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)
                space_num3=space_num3+1
                for str_tmp in str_tmp_l:
                    write_file(str_space, str_tmp)

                if (val1_alloc + val2_alloc + val3_alloc) != 32:
                    print("error32")
                    print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                if (val4_alloc + val5_alloc + val6_alloc) != 32:
                    print("error33")
                    print("val4", val4_alloc, "val5", val5_alloc, "val6", val6_alloc)
 

        # 3,4,6,7,8,9
        if (val1_flag == True) and (val2_flag == False) and (val3_flag == False) and (val4_flag == False) and (val5_flag == False) and (val6_flag == True):
            space_num=space_num+1
            val1_alloc = r_size
            val6_alloc = r_size
            val2_val3_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val2_val3_comb in val2_val3_comb_l:
                val2_alloc,*_ = val2_val3_comb
                val3_alloc = num_pe_row-r_size - val2_alloc

                val4_val5_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
                for val4_val5_comb in val4_val5_comb_l:
                    val4_alloc,*_ = val4_val5_comb
                    val5_alloc = num_pe_row - r_size - val4_alloc

                    str_space = get_space_str(6,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
                    str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)
                    space_num3=space_num3+1
                    for str_tmp in str_tmp_l:
                        write_file(str_space, str_tmp)

                    if (val1_alloc + val2_alloc + val3_alloc) != 32:
                        print("error34")
                        print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                    if (val4_alloc + val5_alloc + val6_alloc) != 32:
                        print("error35")
                        print("val4", val4_alloc, "val5", val5_alloc, "val6", val6_alloc)
 






        # 3,4,6,7,8,9
        if (val1_flag == True) and (val2_flag == False) and (val3_flag == False) and (val4_flag == True) and (val5_flag == False) and (val6_flag == False):
            space_num=space_num+1
            val1_alloc = r_size
            val4_alloc = r_size
            val2_val3_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val2_val3_comb in val2_val3_comb_l:
                val2_alloc,*_ = val2_val3_comb
                val3_alloc = num_pe_row - val2_alloc - r_size

                val5_val6_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
                for val5_val6_comb in val5_val6_comb_l:
                    val5_alloc,*_ = val5_val6_comb
                    val6_alloc = num_pe_row - val5_alloc - r_size

                    str_space = get_space_str(6,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
                    str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)

                    space_num3=space_num3+1
                    for str_tmp in str_tmp_l:
                        write_file(str_space, str_tmp)

                    if (val1_alloc + val2_alloc + val3_alloc) != 32:
                        print("error36")
                        print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                    if (val4_alloc + val5_alloc + val6_alloc) != 32:
                        print("error37")
                        print("val4", val4_alloc, "val5", val5_alloc, "val6", val6_alloc)
 

        # 3,4,6,7,8,9
        if (val1_flag == True) and (val2_flag == False) and (val3_flag == False) and (val4_flag == False) and (val5_flag == True) and (val6_flag == False):
            space_num=space_num+1
            val1_alloc = r_size
            val5_alloc = r_size
            val2_val3_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
            for val2_val3_comb in val2_val3_comb_l:
                val2_alloc,*_ = val2_val3_comb
                val3_alloc = num_pe_row - val2_alloc - r_size

                val4_val6_comb_l=list(itertools.combinations(range(1,num_pe_row-r_size),1))
                for val4_val6_comb in val4_val6_comb_l:
                    val4_alloc,*_ = val4_val6_comb
                    val6_alloc = num_pe_row - val4_alloc - r_size

                    str_space = get_space_str(6,val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
                    str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)

                    space_num3=space_num3+1
                    for str_tmp in str_tmp_l:
                        write_file(str_space, str_tmp)

                    if (val1_alloc + val2_alloc + val3_alloc) != 32:
                        print("error38")
                        print("val1", val1_alloc, "val2", val2_alloc, "val3", val3_alloc)

                    if (val4_alloc + val5_alloc + val6_alloc) != 32:
                        print("error39")
                        print("val4", val4_alloc, "val5", val5_alloc, "val6", val6_alloc)
 

print("space_num", space_num)
print("space_num2", space_num2)
print("space_num3", space_num3)
print("file_id", file_id)
