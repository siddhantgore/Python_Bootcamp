
def find_pairs_of_numbers(num_list,n):
    
    c=0
    lt=[]
    
    for i in range (0,len(num_list)):
        for j in range(i+1,len(num_list)):
            if(num_list[i]+num_list[j]==n and num_list[i] not in lt and num_list[j] not in lt):
                lt.append(num_list[i])
                lt.append(num_list[j])
                c=c+1
    
    if(len(lt)>1):
        return c
    else:
        return 0

num_list=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print(find_pairs_of_numbers(num_list,n))