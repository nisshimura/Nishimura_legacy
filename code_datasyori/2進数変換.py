def con2dec(target):
    amari = []

    while target != 0:
        amari.append(target % 2)
        target = target // 2

    amari.reverse()
    return amari

print(con2dec(56))
