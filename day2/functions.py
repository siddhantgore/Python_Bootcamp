def test(*a):
    print(a)
    return a[0]
name=test("sid","abhay",50)
print(name)

def test(**a):
    return a
name=test(fname="sid",lname="abhay",age=50,skill=["pyhton","java"])

print(name)