
def sum_of_numbers(list_of_num, filter_func=None):

    list_of_num1=[]
    val=[]
    
    for ele in list_of_num:
        list_of_num1.append(ele)
        
    count=0
    if(filter_func==None):
        for ele in list_of_num1:
            count=count+ele
        return count
    else:
        val=filter_func(list_of_num1)
       
        for ele in val:
            count=count+ele
        return count
        
def even(data):
    lt = []
    for ele in data:
        if(ele % 2 == 0):
            lt.append(ele)
    return lt


def odd(data):
    lt2 = []
    for ele in data:
        if(ele % 2 != 0):
            lt2.append(ele)
    return lt2


sample_data = range(1, 11)

print(sum_of_numbers(sample_data, None))
