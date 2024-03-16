#Long-cut version
#Programs that removes numbers before and after the decimal point, depending on the user's input.
def delete_element(fltnum: float, b_int, a_int: int):
        
    flt_str = str(fltnum)
    before_list = []
    before_dec_list = []
    before_final_list = []
    after_list = []
    after_dec_list = []
    after_final_list = []
    index_before = b_int
    index_after = a_int 
    
    fltnumber = flt_str.split('.')
    before_list.append(fltnumber[0])
    print(f'Before list1: {before_list}')
    after_list.append(fltnumber[1])
    print(f'After list1: {after_list}')
    
    for i in before_list:
        convert_before_list = str(i)
        for j in convert_before_list:
            before_dec_list.append(j)
        del before_dec_list[0:index_before]
        print(f'This is the before_dec_list: {before_dec_list}')

     
    for k in after_list:
        convert_after_list = str(k)
        for l in convert_after_list:
            after_dec_list.append(l)
        del after_dec_list[-index_after:]
    print(after_dec_list)
    
  
    for m in before_dec_list:
        before_final_list.append(m)
    before_final_list.append('.')
    print(before_final_list)
        
    for n in after_dec_list:
        after_final_list.append(n)
    print(after_final_list)
        
    final_list = before_final_list + after_final_list
    print(final_list)
    
    for o in final_list:
        print(o, end = '')
    
delete_element(12345.678915, 3, 2)