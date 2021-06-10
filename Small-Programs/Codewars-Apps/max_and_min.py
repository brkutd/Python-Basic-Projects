def high_and_low(numbers):
    lst = list(map(int, numbers.split()))
    max_min = [max(lst), min(lst)]
    max_min_str = str(max_min)[1:-1]
    return "".join(max_min_str.replace(',', ''))


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
