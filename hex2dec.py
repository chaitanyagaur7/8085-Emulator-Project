def hex2dec(a: str) -> int:
    l = len(a)
    i = 0
    dec = 0
    p = 16 ** (l - 1)

    while i < l:
        temp = 0

        if a[i].isdigit():
            temp = int(a[i])
        else:
            temp = {
                "A": 10,
                "B": 11,
                "C": 12,
                "D": 13,
                "E": 14,
                "F": 15
            }.get(a[i].upper(), -1)

            if temp == -1:
                return -1

        dec += p * temp
        i += 1
        p //= 16

    return dec
