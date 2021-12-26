
def Sum(num):
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=int(num/10)
            
    return sum

def find_max(num1, num2):
    max_num=-1
    lt=[]
    
    if(num1<num2):
        for i in range(num1,num2+1):
            if(i%5==0 and Sum(i)%3==0):
                if(i>9 and i<99):
                    lt.append(i)
    
    else:
        return max_num
        
    if(len(lt)>0):
        return lt[-1]
    else:
        return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)