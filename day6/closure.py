def outerFunc(a):
    y=10
    def innerFunc():
        print(a)
        print(y)

    return innerFunc

func=outerFunc(20) #It is a record that stores a function together with an environment
func()    #As observed from the above code, closures help to invoke functions outside their scope.
          #the function innerFunction has its scope only inside the outerFunction. But with the use of closures, we can easily extend its scope to invoke a function outside its scope.