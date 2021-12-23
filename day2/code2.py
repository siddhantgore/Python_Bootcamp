
def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if(num1+num2>=num3 or num3+num2>=num1 or num1+num3>=num2):
        return failure
    elif(num2<=0 or num1<=0 or num3<=0):
        return failure
    else:
        return success

num1=5
num2=3
num3=3
print(form_triangle(num1, num2, num3))