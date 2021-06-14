# Complete the solution so that it reverses all of the words within the string passed in.
# Example:
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    s_lst = s.split()
    s_reversed = s_lst[::-1]
    return " ".join(s_reversed)


print(reverse_words("The greatest victory is that which requires no battle"))
