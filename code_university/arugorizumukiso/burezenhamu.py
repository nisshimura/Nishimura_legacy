x1 = 1
y1 = 1

x2 = 3
y2 = 2

dx = x2 -x1
dy = y2 -y1

f = 2+2*dy-dx
print("first f : "+str(f))
for i in range(1,dx+1):
    print("x1,y1 : "+str(x1)+","+str(y1))
    while f>=0:
        y1 += 1
        f -= 2*dx
        print("while f : "+str(f))
        
    x1 += 1
    f += 2*dy
    print("for f : "+str(f))
print("x2,y2 : "+str(x2)+","+str(y2))
