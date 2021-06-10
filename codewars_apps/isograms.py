# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    test_list = []
    for letter in string:
        if letter.lower() not in test_list:
            test_list.append(letter.lower())
    string2 = "".join(test_list)
    return string2 == string.lower()



is_isogram("isogram")
