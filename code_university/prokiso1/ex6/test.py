
aTap = ((132,'afa'),(2234,'baf'),(324,'caf'))

def get_data(aTap):
    nums = ()
    words = ()
    for t in aTap:
        nums = nums + (t[0],)
        if  t[1] not in words:
            words = words + (t[1],)
    print(nums)
    print(words)
get_data(aTap)

def always_sunny(t1,t2):
    sun = ('sunny', 'sun')
    first = t1[0] + t2[0]
    return (sun[0], first)

print(always_sunny(('cloudy'),('cold',)))