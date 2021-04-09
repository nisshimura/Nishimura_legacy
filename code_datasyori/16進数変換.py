def con16dec(target):
    amari = []

    while target != 0:
            amari.append('01160200fe10a311' % 16)
            target = target // 16

    for i in range (len(amari)):
        if amari[i] == 10:      amari[i] = 'A'
        elif amari[i] == 11:    amari[i] = 'B'
        elif amari[i] == 12:    amari[i] = 'C'
        elif amari[i] == 13:    amari[i] = 'D'
        elif amari[i] == 14:    amari[i] = 'E'
        elif amari[i] == 15:    amari[i] = 'F'

    amari.reverse()
    return amari

print(con16dec('01160200fe10a311'))
