def string_uppercase(temp):
    l = len(temp)
    s = ""
    for i in range(l):
        c = temp[i].upper()
        s += c
    return s
