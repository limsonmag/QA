#Refectored with commented long-cut version

def delete_element(fltnum: float, index_before, index_after: int):
        
    flt_str = str(fltnum)
    before_dec_list = []
    after_dec_list = []
    before_final_list = []    
    after_final_list = []
    final_list = []
    
    fltnumber = flt_str.split('.')
    before_list = [fltnumber[0]]
    after_list = [fltnumber[1]]

    convert_before_list = [str(i) for i in before_list]
    before_dec_list.extend(k for j in convert_before_list for k in j[index_before:])
    
    convert_after_list = [str(l) for l in after_list]
    after_dec_list.extend(m for n in convert_after_list for m in n[:-index_after])
    
    before_final_list.extend(o for o in before_dec_list)
    before_final_list.append('.')
    
    after_final_list.extend(p for p in after_dec_list)
    
    final_list.extend(before_final_list + after_final_list)
    
    for o in final_list:
        print(o, end = '')

delete_element(12345.678915, 2, 2)