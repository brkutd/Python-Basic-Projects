def is_palindrome():
    wrd1 = input()
    wrd2 = wrd1[::-1]
    if wrd1.lower() == wrd2.lower():
        print(True)
    else:
        print(False)


is_palindrome()
