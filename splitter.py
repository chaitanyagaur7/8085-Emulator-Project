def splitter(temp):
    v = []
    res = temp
    delimiter = " ,"
    pch = res.split(delimiter)
    for var in pch:
        v.append(var)
    return v
