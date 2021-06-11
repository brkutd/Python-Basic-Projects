# Your task is to make a function that can take any non-negative integer as an argument
# and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    number = list(str(num))
    if len(number) == 1:
        num_sorted = "".join(number)
        return int(num_sorted)
    for j in range(len(number) - 1, 0, -1):
        for i in range(j):
            if number[i] < number[i + 1]:
                number[i], number[i + 1] = number[i + 1], number[i]
    num_sorted = "".join(number)
    return int(num_sorted)

