

def encrypt_sentence(sentence):
    
    temp=[]
    vowel=[]
    consonants=[]
    database=["a","e","i","o","u"]
    new_sentence=list(sentence)
    for ele in new_sentence:
        if((new_sentence.index(ele))+1%2!=0):
            new_sentence[new_sentence.index(ele)]=ele[::-1]
        else:
            for char in ele:
                if(char in database):
                    vowel.append(char)
                else:
                    consonants.append(char)
            new_sentence[new_sentence.index(ele)]="".join(consonants+vowel)
            
    return("".join(new_sentence))    

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)