# Write a function that will check if two given characters are the same case.
# If any of characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters and not the same case, return 0

def same_case(a, b):
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    elif not a.isalpha() or not b.isalpha():
        return -1
    else:
        return 0
    pass

print(same_case('A', 's'))
