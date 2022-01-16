def minindexword(words):
    loop = 0
    index = 0
    mini = words[index]
    while loop + 1 < len(words):
        if mini > words[index + 1]:
            mini = words[index + 1]
        loop += 1
        index += 1
    return words.index(mini)


def maxindexword(words):
    loop = 0
    index = 0
    maxi = words[index]
    while loop + 1 < len(words):
        if maxi < words[index + 1]:
            maxi = words[index + 1]
        loop += 1
        index += 1
    return words.index(maxi)


def sorting(words, order):
    index = 0
    if order != "<" and order != ">":
        print(None)
    if order == "<":
        while index < len(words):
            temp = words[index]
            words[index] = words[minindexword(words[index:len(words)])]
            words[minindexword(words[index:len(words)])] = temp
            index += 1
        print(words)
    if order == ">":
        while index < len(words):
            temp = words[index]
            words[index] = words[maxindexword(words[index:len(words)])]
            words[maxindexword(words[index:len(words)])] = temp
            index += 1
        print(words)


sorting([2, 3, 4, 1], "<")
