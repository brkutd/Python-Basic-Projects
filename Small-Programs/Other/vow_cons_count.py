def vow_cons_count():
    word = input()
    vowels = 0
    cons = 0
    for i in word:
        if i in "aeiouyAEIOUY":
            vowels += 1
        else:
            cons += 1
    print("Vowels:", vowels)
    print("Consonants:", cons)
