
def encode(message):
    count=1
    ans=[]
    message=list(message)
    new_message=message
    new_message.append("0")
    
    for i in range(0,len(message)-1):
        if(message[i]==new_message[i+1]):
            count=count+1
        else:
            ans.append(str(count))
            ans.append(message[i])
            count=1
            
    return ("".join(ans))

encoded_message=encode("AABCCA")
print(encoded_message)