def amount(a):
    if not isinstance(a, int):
        return [-1,-1,-1]
    elif a >= 14 :
        J = HO = a//14
        remainingINR = a % 14
        ji = remainingINR * 34
        return [J,HO,ji]
    else:
        return [-1,-1,-1]

print(amount(100))
