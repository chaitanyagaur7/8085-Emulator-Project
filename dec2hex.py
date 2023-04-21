def dec2hex(n, size):
    str_ = ""
    if n == 0 and size == 2:
        str_ = "00"
    elif n == 0 and size == 4:
        str_ = "0000"
    else:
        while n != 0:
            r = n % 16
            n = n // 16
            if 0 <= r <= 9:
                str_ += chr(r + 48)
            else:
                if r == 10:
                    str_ += 'A'
                elif r == 11:
                    str_ += 'B'
                elif r == 12:
                    str_ += 'C'
                elif r == 13:
                    str_ += 'D'
                elif r == 14:
                    str_ += 'E'
                elif r == 15:
                    str_ += 'F'
        i = len(str_)
        for j in range(i // 2):
            temp = str_[j]
            str_[j] = str_[i - j - 1]
            str_[i - j - 1] = temp
        if size == 2:
            if i == 2:
                return str_
            else:
                str_ = "0" + str_
        elif size == 4:
            if i == 4:
                return str_
            elif i == 3:
                str_ = "0" + str_
            elif i == 2:
                str_ = "00" + str_
            elif i == 1:
                str_ = "000" + str_
    return str_
