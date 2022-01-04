#decorators in python

def xyz(func):
    def inner1(a,b):
        print("---------")
        func(a,b)
        print("---------")
    return inner1
def pqs(func):
    def inner1(a,b):
        print("^^^^^^^^^^")
        func(a,b)
        print("++++++++++")
    return inner1

@xyz     #decorators wraps the data inside it
@pqs
def sample(a,b):
    print(a,b)

sample("dummy","data")