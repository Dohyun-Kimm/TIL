from pyrsistent import b


T = int(input())
power = 3**T
a_string = '-'* power


def cantor(a):
    pass
    cut = len(a)
    if len(a) ==1:
        return b
    else:
        a1,a2,a3 = a[::,]
        return cantor(a1) + cantor(a2) +cantor(a3)