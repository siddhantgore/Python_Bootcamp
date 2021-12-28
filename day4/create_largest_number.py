

def create_largest_number(number_list):
    ans=""
    number_list.sort()
    number_list=number_list[::-1]
    for ele in number_list:
        ans+=str(ele)
    return int(ans)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)