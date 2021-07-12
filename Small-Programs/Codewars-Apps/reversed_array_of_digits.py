# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    num = list(map(int, str(n)))
    return num[::-1]

print(digitize(1234))
