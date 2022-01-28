import itertools
import math

r_size=3
s_size=3
file_id=1
num_pe_col=64
num_pe_row=64

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
            print("val1_alloc", val1_alloc, "val2_alloc", val2_alloc, "val3_alloc", val3_alloc, "val4_alloc", val4_alloc, "val5_alloc", val5_alloc, "val6_alloc", val6_alloc)
            print("inner most loop val comb_obj", comb_obj)
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

def process_write_val6(val_permu_l1, val_permu_l2, num_id):
    print("process_write_val6", num_id)
    for val_permu1 in val_permu_l1:
        val1 = val_permu1[0][0]
        val2 = val_permu1[1][0]
        val3 = val_permu1[2][0]
        val1_alloc = val_permu1[0][1]
        val2_alloc = val_permu1[1][1]
        val3_alloc = val_permu1[2][1]
        for val_permu2 in val_permu_l2:
            val4 = val_permu2[0][0]
            val5 = val_permu2[1][0]
            val6 = val_permu2[2][0]
            val4_alloc = val_permu2[0][1]
            val5_alloc = val_permu2[1][1]
            val6_alloc = val_permu2[2][1]
            str_space = get_space_str(6,val1, val2, val3, val4, val5, val6, val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,val6_alloc)
            str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, val6, val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, val6_alloc)
            for str_tmp in str_tmp_l:
               write_file(str_space, str_tmp)

def process_write_val5(val_permu_l1, val_permu_l2, num_id):
    print("process_write_val5", num_id)
    for val_permu1 in val_permu_l1:
        print("val_permu1")
        print(val_permu1)
        val1 = val_permu1[0][0]
        val2 = val_permu1[1][0]
        val3 = val_permu1[2][0]
        val1_alloc = val_permu1[0][1]
        val2_alloc = val_permu1[1][1]
        val3_alloc = val_permu1[2][1]
        for val_permu2 in val_permu_l2:
            val4 = val_permu2[0][0]
            val5 = val_permu2[1][0]
            val4_alloc = val_permu2[0][1]
            val5_alloc = val_permu2[1][1]
            str_space = get_space_str(5,val1, val2, val3, val4, val5, 'ng', val1_alloc,val2_alloc,val3_alloc,val4_alloc,val5_alloc,0)
            str_tmp_l = get_tmp_str(val1, val2, val3, val4, val5, "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, val5_alloc, 0)
            for str_tmp in str_tmp_l:
               write_file(str_space, str_tmp)


def process_write_val4(val_permu_l1, val_permu_l2, num_id):
    print("process_write_val4",num_id)
    for val_permu1 in val_permu_l1:
        val1 = val_permu1[0][0]
        val2 = val_permu1[1][0]
        val1_alloc = val_permu1[0][1]
        val2_alloc = val_permu1[1][1]
        for val_permu2 in val_permu_l2:
            val3 = val_permu2[0][0]
            val4 = val_permu2[1][0]
            val3_alloc = val_permu2[0][1]
            val4_alloc = val_permu2[1][1]
            str_space = get_space_str(4,val1, val2, val3, val4, 'ng', 'ng', val1_alloc,val2_alloc,val3_alloc,val4_alloc,0,0)
            str_tmp_l = get_tmp_str(val1, val2, val3, val4, "ng", "ng", val1_alloc, val2_alloc, val3_alloc, val4_alloc, 0, 0)
            for str_tmp in str_tmp_l:
               write_file(str_space, str_tmp)
        
def process_write_val3(val_permu_l, val3_alloc, num_id):
    print("process_write_val3", num_id)
    for val_permu in val_permu_l:
        val1 = val_permu[0][0]
        val2 = val_permu[1][0]
        val1_alloc = val_permu[0][1]
        val2_alloc = val_permu[1][1]
        str_space = get_space_str(3,val1, val2, val3, 'ng', 'ng', 'ng', val1_alloc,val2_alloc,val3_alloc,0,0,0)
        str_tmp_l = get_tmp_str(val1, val2, val3, "ng", "ng", "ng", val1_alloc, val2_alloc, val3_alloc, 0, 0, 0)
        for str_tmp in str_tmp_l:
            write_file(str_space, str_tmp)

# print 
def get_space_str(dim_num, val1, val2, val3, val4, val5, val6, val1_alloc=0, val2_alloc=0, val3_alloc=0, val4_alloc=0, val5_alloc=0, val6_alloc=0):
    print("get_space_str")
    # num val = 3
    prefix="{S[n,k,c,ox,oy,rx,ry]->PE["
    suffix="]}"
    space_str_tmp = ""
    if dim_num == 3:
        if val1 == 'rx' or val1 == 'ry':
            space_str = val1
        else:
            space_str=val1+"%"+str(val1_alloc)

        if val2 == 'rx' or val2 == 'ry':
            space_str=space_str+"+"+str(val1_alloc)+"*"+val2
        else:
            space_str=space_str+"+"+str(val1_alloc)+"*("+val2+"%"+str(val2_alloc)+")"

        if val3 == 'rx' or val3 == 'ry':
            space_str=space_str+","+val3
        else:
            space_str=space_str+","+val3+"%"+str(val3_alloc)
        space_str_tmp = prefix+space_str+suffix

    if dim_num == 4:
        if val1 == 'rx' or val1 == 'ry':
            space_str=val1
        else:
            space_str=val1+"%"+str(val1_alloc)

        if val2 == 'rx' or val2 == 'ry':
            space_str=space_str+"+"+str(val1_alloc)+"*"+val2
        else:
            space_str=space_str+"+"+str(val1_alloc)+"*("+val2+"%"+str(val2_alloc)+")"

        if val3 == 'rx' or val3 == 'ry':
            space_str=space_str+","+val3
        else:
            space_str=space_str+","+val3+"%"+str(val3_alloc)

        if val4 == 'rx' or val4 == 'ry':
            space_str=space_str+"+"+str(val3_alloc)+"*("+val4
        else:
            space_str=space_str+"+"+str(val3_alloc)+"*("+val4+"%"+str(val4_alloc)+")"
        space_str_tmp = prefix+space_str+suffix

    if dim_num == 5:
        tmp_alloc = val1_alloc * val2_alloc

        if val1 == 'rx' or val1 == 'ry':
            space_str=val1
        else:
            space_str=val1+"%"+str(val1_alloc)

        if val2 == 'rx' or val2 == 'ry':
            space_str=space_str+"+"+str(val1_alloc)+"*"+val2+"+"
        else:
            space_str=space_str+"+"+str(val1_alloc)+"*("+val2+"%"+str(val2_alloc)+")+"

        if val3 == 'rx' or val3 == 'ry':
            space_str=space_str+str(tmp_alloc)+"*"+val3
        else:
            space_str=space_str+str(tmp_alloc)+"*("+val3+"%"+str(val3_alloc)+")"

        if val4 == 'rx' or val4 == 'ry':
            space_str=space_str+","+val4
        else:
            space_str=space_str+","+val4+"%"+str(val4_alloc)

        if val5 == 'rx' or val5 == 'ry':
            space_str=space_str+"+"+str(val4_alloc)+val5
        else:
            space_str=space_str+"+"+str(val4_alloc)+"*("+val5+"%"+str(val5_alloc)+")"

        space_str_tmp = prefix+space_str+suffix
    if dim_num == 6:
        tmp_alloc = val1_alloc * val2_alloc
        if val1 == 'rx' or val1 == 'ry':
            space_str=val1
        else:
            space_str=val1+"%"+str(val1_alloc)

        if val2 == 'rx' or val2 == 'ry':
            space_str=space_str+"+"+str(val1_alloc)+"*"+val2+"+"
        else:
            space_str=space_str+"+"+str(val1_alloc)+"*("+val2+"%"+str(val2_alloc)+")+"

        if val3 == 'rx' or val3 == 'ry':
            space_str=space_str+str(tmp_alloc)+"*"+val3
        else:
            space_str=space_str+str(tmp_alloc)+"*("+val3+"%"+str(val3_alloc)+")"

        tmp_alloc = val4_alloc * val5_alloc
        if val4 == 'rx' or val4 == 'ry':
            space_str=space_str+","+val4+"+"
        else:
            space_str=space_str+","+val4+"%"+str(val4_alloc)+"+"

        if val5 == 'rx' or val5 == 'ry':
            space_str=space_str+str(val4_alloc)+"*"+val5+"+"
        else:
            space_str=space_str+str(val4_alloc)+"*("+val5+"%"+str(val5_alloc)+")+"

        if val6 == 'rx' or val6 == 'ry':
            space_str=space_str+str(tmp_alloc)+"*"+val6
        else:
            space_str=space_str+str(tmp_alloc)+"*("+val6+"%"+str(val6_alloc)+")"
        space_str_tmp = prefix+space_str+suffix
    print(space_str_tmp)
    return space_str_tmp

print("num val = 3")
space_num=0
space_num2 = 0
print("------")
dim_sel_l=[('rx','ry','c'),('rx','c','ry'),('rx','ry','k'),('rx','k','ry')]
print(dim_sel_l) 
for dim_sel_obj in dim_sel_l:
    space_num2 = space_num2 + 1
    print("dim_sel_obj", dim_sel_obj)
    val1, val2, val3, *_ = dim_sel_obj

    print(val1, val2, val3)

    if (val1 == 'rx') and (val2 == 'ry') and ((val3 == 'c') or (val3 == 'k')):
        val1_alloc=r_size
        val2_alloc=r_size
        val3_alloc = num_pe_row
        space_num2 = space_num2 + 1
        val_permu_l = [((val1,val1_alloc),(val2, val2_alloc))]
        process_write_val3(val_permu_l, val3_alloc, space_num)

    elif (val1 == 'rx') and ((val2 == 'c') or (val2 == 'k')) and (val3 == 'ry'):
        val1_alloc=r_size
        val2_alloc=int(math.floor(num_pe_row/r_size))
        val3_alloc =r_size
        space_num2 = space_num2 + 1
        val_tuple_l = [(val1,val1_alloc),(val2, val2_alloc)]
        val_permu_l = list(itertools.permutations(val_tuple_l))
        process_write_val3(val_permu_l, val3_alloc, space_num)
        
    else:
        print("exit process space val3")
        exit(1)



print("space_num", space_num)
print("space_num2", space_num2)

print("num val = 4")
space_num=0
space_num2=0

print("------")
dim_sel_l=[('rx','ry','ox','oy'),('rx','ox','ry','oy'),('rx','ry','c','k'),('rx','c','ry','k')]
print(dim_sel_l) 
for dim_sel_obj in dim_sel_l:
    space_num2 = space_num2 + 1
    val1, val2, val3, val4, *_ = dim_sel_obj
    print("val1", "val2", "val3", "val4")
    print(val1, val2, val3, val4)

    if ((val1 == 'rx') and (val2 == 'ry') and (val3 == 'ox') and (val4 == 'oy')):
        val1_alloc = r_size
        val2_alloc = r_size
        space_num = space_num + 1
        for val3_alloc in range(2,int(num_pe_row/2)+1):
            val4_alloc = int(math.floor(num_pe_row/val3_alloc))
            if (val3_alloc < 2)  or (val4_alloc < 2) or (val3_alloc*val4_alloc > num_pe_row):
                continue
            val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc))]
            val_permu_l2 = [((val3,val3_alloc),(val4,val4_alloc))]
            process_write_val4(val_permu_l1, val_permu_l2, space_num)

    elif ((val1 == 'rx') and (val2 == 'ry') and (val3 == 'c') and (val4 == 'k')):
        val1_alloc = r_size
        val2_alloc = r_size
        space_num = space_num + 1

        for val3_alloc in range(2,int(num_pe_row/2)+1):
            val4_alloc = int(math.floor(num_pe_row/val3_alloc))
            if (val3_alloc < 2)  or (val4_alloc < 2) or (val3_alloc*val4_alloc > num_pe_row):
                continue
            val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc))]
            val_tuple_l2 = [(val3,val3_alloc),(val4, val4_alloc)]
            val_permu_l2 = list(itertools.permutations(val_tuple_l2))
            process_write_val4(val_permu_l1, val_permu_l2, space_num)
        
    elif ((val1 == 'rx') and (val2 == 'ox') and (val3 == 'ry') and (val4 == 'oy')) or \
            ((val1 == 'rx') and (val2 == 'c') and (val3 == 'ry') and (val4 == 'k')):
        val1_alloc = r_size
        val2_alloc = int(math.floor(num_pe_row/r_size))
        val3_alloc = r_size
        val4_alloc = int(math.floor(num_pe_row/r_size))
        space_num = space_num + 1

        val_tuple_l1 = [(val1,val1_alloc),(val2, val2_alloc)]
        val_permu_l1 = list(itertools.permutations(val_tuple_l1))
        val_tuple_l2 = [(val3,val3_alloc),(val4, val4_alloc)]
        val_permu_l2 = list(itertools.permutations(val_tuple_l2))
        process_write_val4(val_permu_l1, val_permu_l2, space_num)

    else:
        print("process write4 val error")
        exit(1)
 
print("num val = 5")
space_num=0
space_num2=0

print("------")
dim_sel_l=[('rx','ry','ox','oy','k'),('rx','ry','k','ox','oy'),('rx','ox','oy','ry','k'),('rx','ox','k','ry','oy'),\
        ('ox','oy','k','rx','ry'),('rx','ry','ox','oy','c'),('rx','ry','c','ox','oy'),('rx','ox','oy','ry','c'),('rx','ox','c','ry','oy'),('ox','oy','c','rx','ry')]

print(dim_sel_l) 
for dim_sel_obj in dim_sel_l:
    space_num2=space_num2+1
    print(dim_sel_obj) 
    val1, val2, val3, val4, val5 = dim_sel_obj

    print("val1", "val2", "val3", "val4", "val5")
    print(val1, val2, val3, val4, val5)

    space_num=space_num+1

    if (val1 == 'rx') and (val2 == 'ry') and (val3 == 'ox') and (val4 == 'oy') and ((val5 == 'k') or (val5 == 'c')):
        val1_alloc = r_size
        val2_alloc = r_size
        val3_alloc = int(math.floor(num_pe_row / (r_size*r_size)))
        space_num = space_num + 1

        for val4_alloc in range(2,int(num_pe_row/2)):
            val5_alloc = int(math.floor(num_pe_row/val4_alloc))
            if (val4_alloc < 2)  or (val5_alloc < 2) or (val4_alloc*val5_alloc > num_pe_row):
                continue
            val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)),\
                            ((val1,val1_alloc),(val3,val3_alloc),(val2,val2_alloc)), \
                            ((val3,val3_alloc),(val1,val1_alloc),(val2,val2_alloc))]
            val_tuple_l2 = [(val4,val4_alloc),(val5, val5_alloc)]
            val_permu_l2 = list(itertools.permutations(val_tuple_l2))

            process_write_val5(val_permu_l1, val_permu_l2, space_num)

    elif (val1 == 'rx') and (val2 == 'ry') and ((val3 == 'k') or (val3 == 'c')) and (val4 == 'ox') and (val5 == 'oy'): 
        val1_alloc = r_size
        val2_alloc = r_size
        val3_alloc = int(math.floor(num_pe_row / (r_size*r_size)))
        space_num = space_num + 1

        for val4_alloc in range(2,int(num_pe_row/2)):
            val5_alloc = int(math.floor(num_pe_row/val4_alloc))
            if (val4_alloc < 2)  or (val5_alloc < 2) or (val4_alloc*val5_alloc > num_pe_row):
                continue
            val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)),\
                    ((val1,val1_alloc),(val3,val3_alloc),(val2,val2_alloc)), \
                    ((val3,val3_alloc),(val1,val1_alloc),(val2,val2_alloc))]
            val_permu_l2 = [((val4,val4_alloc),(val5,val5_alloc))]
            process_write_val5(val_permu_l1, val_permu_l2,space_num)

    elif (val1 == 'rx') and (val2 == 'ox') and (val3 == 'oy') and (val4 == 'ry') and ((val5 == 'k') or (val5 == 'c')): 
        val1_alloc = r_size
        val4_alloc = r_size
        val5_alloc = int(math.floor(num_pe_row/r_size))
        space_num = space_num + 1

        for val2_alloc in range(2,int(num_pe_row/(2*r_size))):
            val3_alloc = int(math.floor(num_pe_row/(val2_alloc*r_size)))
            if (val2_alloc < 2)  or (val3_alloc < 2) or (val1_alloc*val2_alloc*val3_alloc > num_pe_row):
                continue
            val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)),\
                            ((val2,val2_alloc),(val1,val1_alloc),(val3,val3_alloc)), \
                            ((val2,val2_alloc),(val3,val3_alloc),(val1,val1_alloc))]
            val_tuple_l2 = [(val4,val4_alloc),(val5, val5_alloc)]
            val_permu_l2 = list(itertools.permutations(val_tuple_l2))
            process_write_val5(val_permu_l1, val_permu_l2,space_num)

    elif (val1 == 'rx') and (val2 == 'ox') and ((val3 == 'k') or (val3 == 'c')) and (val4 == 'ry') and (val5 == 'oy'): 
        val1_alloc = r_size
        val4_alloc = r_size
        val5_alloc = int(math.floor(num_pe_row/r_size))
        space_num = space_num + 1

        for val2_alloc in range(2,int(num_pe_row/(2*r_size))):
            val3_alloc = int(math.floor(num_pe_row/(val2_alloc*r_size)))
            if (val2_alloc < 2)  or (val3_alloc < 2) or (val1_alloc*val2_alloc*val3_alloc > num_pe_row):
                continue
            val_tuple_l1 = [(val1,val1_alloc),(val2, val2_alloc),(val3, val3_alloc)]
            val_permu_l1 = list(itertools.permutations(val_tuple_l1))
            val_tuple_l2 = [(val4,val4_alloc),(val5, val5_alloc)]
            val_permu_l2 = list(itertools.permutations(val_tuple_l2))

            process_write_val5(val_permu_l1, val_permu_l2, space_num)

    elif (val1 == 'ox') and (val2 == 'oy') and ((val3 == 'k') or (val3 == 'c')) and (val4 == 'rx') and (val5 == 'ry'): 
        val4_alloc = r_size
        val5_alloc = r_size
        val3_alloc = int(math.floor(num_pe_row/(r_size*r_size)))
        space_num = space_num + 1

        for val1_alloc in range(2,int(num_pe_row/2)):
            for val2_alloc in range(2,int(num_pe_row/val2_alloc)):
                val3_alloc = int(math.floor(num_pe_row/(val1_alloc*val2_alloc)))
                if (val1_alloc < 2) or (val2_alloc < 2)  or (val3_alloc < 2) or (val1_alloc*val2_alloc*val3_alloc > num_pe_row):
                    continue
                val_tuple_l1 = [((val1,val1_alloc),(val2, val2_alloc),(val3, val3_alloc)),\
                                ((val1,val1_alloc),(val3, val3_alloc),(val2, val2_alloc)),\
                                ((val3,val3_alloc),(val1, val1_alloc),(val2, val2_alloc))]
                val_tuple_l2 = [((val4,val4_alloc),(val5, val5_alloc))]
                process_write_val5(val_permu_l1, val_permu_l2, space_num)
    else:
        print("process write5 val error")
        exit(1)

print("num val = 6")

print("------")
dim_sel_l=[('rx','ry','ox','oy','c','k'),('rx','ry','c','ox','oy','k'),('rx','ry','k','ox','oy','c'),\
        ('rx','ox','oy','ry','c','k'),('rx','c','k','ry','ox','oy'),('rx','ox','c','ry','oy','k')]

print(dim_sel_l) 
for dim_sel_obj in dim_sel_l:
    space_num2=space_num2+1
    print(dim_sel_obj) 
    val1, val2, val3, val4, val5, val6 = dim_sel_obj
    print("val1", "val2", "val3", "val4", "val5", "val6")
    print(val1, val2, val3, val4, val5, val6)

    if (val1 == 'rx') and (val2 == 'ry') and (val3 == 'ox') and (val4 == 'oy') and (val5 == 'c') and (val6 == 'k'):
        val1_alloc = r_size
        val2_alloc = r_size
        val3_alloc = int(math.floor(num_pe_row / (r_size*r_size)))
        space_num = space_num + 1
        for val4_alloc in range(2,int(num_pe_row/2)):
            for val5_alloc in range(2,int(num_pe_row/val4_alloc)):
                val6_alloc = int(math.floor(num_pe_row/(val4_alloc*val5_alloc)))
                if (val4_alloc < 2) or (val5_alloc < 2)  or (val6_alloc < 2) or (val4_alloc*val5_alloc*val6_alloc > num_pe_row):
                    continue
                val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)),\
                                ((val1,val1_alloc),(val3,val3_alloc),(val2,val2_alloc)), \
                                ((val3,val3_alloc),(val1,val1_alloc),(val2,val2_alloc))]
                val_tuple_l2 = [(val4,val4_alloc),(val5, val5_alloc),(val6, val6_alloc)]
                val_permu_l2 = list(itertools.permutations(val_tuple_l2))
                process_write_val6(val_permu_l1, val_permu_l2, space_num)

    elif (val1 == 'rx') and (val2 == 'ry') and (val3 == 'c') and (val4 == 'ox') and (val5 == 'oy') and (val6 == 'k'):
        val1_alloc = r_size
        val2_alloc = r_size
        val3_alloc = int(math.floor(num_pe_row / (r_size*r_size)))
        space_num = space_num + 1
        for val4_alloc in range(2,int(num_pe_row/2)):
            for val5_alloc in range(2,int(num_pe_row/val4_alloc)):
                val6_alloc = int(math.floor(num_pe_row/(val4_alloc*val5_alloc)))
                if (val4_alloc < 2) or (val5_alloc < 2)  or (val6_alloc < 2) or (val4_alloc*val5_alloc*val6_alloc > num_pe_row):
                    continue
                val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)),\
                                ((val1,val1_alloc),(val3,val3_alloc),(val2,val2_alloc)), \
                                ((val3,val3_alloc),(val1,val1_alloc),(val2,val2_alloc))]

                val_permu_l2 = [((val4,val4_alloc),(val5,val5_alloc),(val6,val6_alloc)),\
                                ((val4,val4_alloc),(val6,val6_alloc),(val5,val5_alloc)), \
                                ((val6,val6_alloc),(val4,val4_alloc),(val5,val5_alloc))]
                process_write_val6(val_permu_l1, val_permu_l2, space_num)

    elif (val1 == 'rx') and (val2 == 'ry') and (val3 == 'k') and (val4 == 'ox') and (val5 == 'oy') and (val6 == 'c'):
        val1_alloc = r_size
        val2_alloc = r_size
        val3_alloc = int(math.floor(num_pe_row / (r_size*r_size)))
        space_num = space_num + 1
        for val4_alloc in range(2,int(num_pe_row/2)):
            for val5_alloc in range(2,int(num_pe_row/val4_alloc)):
                val6_alloc = int(math.floor(num_pe_row/(val4_alloc*val5_alloc)))
                if (val4_alloc < 2) or (val5_alloc < 2)  or (val6_alloc < 2) or (val4_alloc*val5_alloc*val6_alloc > num_pe_row):
                    continue
                val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)),\
                                ((val1,val1_alloc),(val3,val3_alloc),(val2,val2_alloc)), \
                                ((val3,val3_alloc),(val1,val1_alloc),(val2,val2_alloc))]

                val_permu_l2 = [((val4,val4_alloc),(val5,val5_alloc),(val6,val6_alloc)),\
                                ((val4,val4_alloc),(val6,val6_alloc),(val5,val5_alloc)), \
                                ((val6,val6_alloc),(val4,val4_alloc),(val5,val5_alloc))]
                process_write_val6(val_permu_l1, val_permu_l2, space_num)

    elif (val1 == 'rx') and (val2 == 'ox') and (val3 == 'oy') and (val4 == 'ry') and (val5 == 'c') and (val6 == 'k'):
        val1_alloc = r_size
        val4_alloc = r_size
        space_num = space_num + 1
        for val2_alloc in range(2,int(num_pe_row/2)):
            val3_alloc = int(math.floor(num_pe_row/(val1_alloc*val2_alloc)))
            if (val2_alloc < 2) or (val3_alloc < 2) or (val1_alloc*val2_alloc*val3_alloc > num_pe_row):
                continue
            for val5_alloc in range(2,int(num_pe_row/2)):
                val6_alloc = int(math.floor(num_pe_row/(val4_alloc*val5_alloc)))
                if (val5_alloc < 2) or (val6_alloc < 2) or (val4_alloc*val5_alloc*val6_alloc > num_pe_row):
                    continue
                val_permu_l1 = [((val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)),\
                                ((val2,val2_alloc),(val1,val1_alloc),(val3,val3_alloc)), \
                                ((val2,val2_alloc),(val3,val3_alloc),(val1,val1_alloc))]

                val_tuple_l2 = [(val4,val4_alloc),(val5, val5_alloc),(val6,val6_alloc)]
                val_permu_l2 = list(itertools.permutations(val_tuple_l2))
                process_write_val6(val_permu_l1, val_permu_l2, space_num)

    #5
    elif (val1 == 'rx') and (val2 == 'c') and (val3 == 'k') and (val4 == 'ry') and (val5 == 'ox') and (val6 == 'oy'):
        val1_alloc = r_size
        val4_alloc = r_size
        space_num = space_num + 1
        for val2_alloc in range(2,int(num_pe_row/2)):
            val3_alloc = int(math.floor(num_pe_row/(val1_alloc*val2_alloc)))
            if (val2_alloc < 2) or (val3_alloc < 2) or (val1_alloc*val2_alloc*val3_alloc > num_pe_row):
                    continue
            for val5_alloc in range(2,int(num_pe_row/2)):
                val6_alloc = int(math.floor(num_pe_row/(val4_alloc*val5_alloc)))
                if (val5_alloc < 2) or (val6_alloc < 2) or (val4_alloc*val5_alloc*val6_alloc > num_pe_row):
                    continue
                val_tuple_l1 = [(val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)]
                val_permu_l1 = list(itertools.permutations(val_tuple_l1))

                val_permu_l2 = [((val4,val4_alloc),(val5, val5_alloc),(val6,val6_alloc)),\
                                ((val5,val5_alloc),(val4, val4_alloc),(val6,val6_alloc)),\
                                ((val5,val5_alloc),(val6, val6_alloc),(val4,val4_alloc))]
                process_write_val6(val_permu_l1, val_permu_l2, space_num)

    # 6
    elif (val1 == 'rx') and (val2 == 'ox') and (val3 == 'c') and (val4 == 'ry') and (val5 == 'oy') and (val6 == 'k'):
        val1_alloc = r_size
        val4_alloc = r_size
        space_num = space_num + 1
        for val2_alloc in range(2,int(num_pe_row/2)):
            val3_alloc = int(math.floor(num_pe_row/(val1_alloc*val2_alloc)))
            if (val2_alloc < 2) or (val3_alloc < 2) or (val1_alloc*val2_alloc*val3_alloc > num_pe_row):
                    continue
            for val5_alloc in range(2,int(num_pe_row/2)):
                val6_alloc = int(math.floor(num_pe_row/(val4_alloc*val5_alloc)))
                if (val5_alloc < 2) or (val6_alloc < 2) or (val4_alloc*val5_alloc*val6_alloc > num_pe_row):
                    continue
                val_tuple_l1 = [(val1,val1_alloc),(val2,val2_alloc),(val3,val3_alloc)]
                val_permu_l1 = list(itertools.permutations(val_tuple_l1))
                val_tuple_l2 = [(val4,val4_alloc),(val5,val5_alloc),(val6,val6_alloc)]
                val_permu_l2 = list(itertools.permutations(val_tuple_l2))
                process_write_val6(val_permu_l1, val_permu_l2, space_num)
    else:
        print("process write6 val error")
        exit(1)

