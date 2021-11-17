import datetime

a = '5:00'
b = '8:40'

after = datetime.datetime.strptime(a, '%H:%M')
after2 = datetime.datetime.strptime(b, '%H:%M')
print(after)
print(type(after))
print(after.hour + after2.hour)