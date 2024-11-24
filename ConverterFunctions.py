# основание системы не больше 9!!!

def fromdec(num, base):
    num_ = []
    while num >= base:
        num, r = divmod(num, base)
        num_.insert(0, str(r))
    num_.insert(0, str(num))
    return int(''.join(num_))

def todec(num, base):
    res = 0
    num = list(str(num))
    num.reverse()
    for i in range(0, len(num)):
        res += int(num[i]) * (base**i)
    return res

print(fromdec(123, 2))