

def check_palindrome(word):

    word_list=list(word)
    word_list2=word_list[::-1]
    if("".join(word_list)=="".join(word_list2)):
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")