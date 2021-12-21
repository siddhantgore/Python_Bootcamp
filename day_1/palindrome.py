def palindrome(text:str) -> int:
    text=text.casefold()
    if text[::-1]==text:
        return True
    else:
        return False

print(palindrome("Mom"))