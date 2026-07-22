#input
x1_1 = input("x1=")
y1_1 = input("y1=")
r1_1 = input("radius of the first circle is: ")
x2_1 = input("x2=")
y2_1 = input("y2=")
r2_1 = input("radius of the secound circle is: ")
#processing
x1 = float(x1_1)
y1 = float(y1_1)
r1 = float(r1_1)
x2 = float(x2_1)
y2 = float(y2_1)
r2 = float(r2_1)
#def_new_function
def tnod(x1,y1,r1,x2,y2,r2):
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    R = r1 + r2
    dif = abs(r1-r2)
    if d == 0 and r1 == r2:
        num = "infinitely many"
    elif d**2 > R**2 or d < dif:
        num = "0"
    elif d == R or d == dif:
        num = "1"
    else:
        num = "2"
    return num
#calculation
result = tnod(x1,y1,r1,x2,y2,r2)
print(result)