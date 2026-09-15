#1
#input_and_processing
a_1 = input("a=")
a = float(a_1)
b_1 = input("b=")
b = float(b_1)
c_1 = input("c=")
c = float(c_1)
#type_conversion_and_output
print(f"{int(a)},{int(b)},{int(c)},{float(a)},{float(b)},{float(c)}")


#2
#input
a_1 = input("a=")
b_1 = input("b=")
c_1 = input("c=")
#processing
a = float(a_1)
b = float(b_1)
c = float(c_1)
#calculation_area
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**(1/2)
#calculation_angle
import math
A = math.acos((b**2+c**2-a**2)/(2*b*c))
B = math.acos((a**2+c**2-b**2)/(2*a*c))
C = math.acos((a**2+b**2-c**2)/(2*a*b))
#calculation_circumscribed_circle
R = (a*b*c)/(4*S)
S_1 = (math.pi)*(R**2)
#calculation_incircle
r = S/p
S_2 = (math.pi)*(r**2)
#output
print("The area of the triangle is ",S)
print("A=",A,", B=",B,", C=",C)
print("The radius of the circumscribed circle is ",R)
print("The area of the circumscribed circle is ",S_1)
print("The radius of the incircle is ",r)
print("The area of the incircle is ",S_2)


#3
#input
equa = input("Input any mathematical expression: ")
#calculation
reslt = eval(equa)
#output
print(f"{equa} = {reslt}")


#4
#input
a = float(input("a = "))
b = float(input("b = "))
a , b = b , a
print(b-a)
print(a-b)


#5
#as above


#6
#import
import math
#def_function_area
def area(a,b,c):
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print(S)
#def_function_angle
def angle(a,b,c):
    A = math.acos((b**2+c**2-a**2)/(2*b*c))
    B = math.acos((a**2+c**2-b**2)/(2*a*c))
    C = math.acos((a**2+b**2-c**2)/(2*a*b))
    print(f"{A},{B},{C}")
#def_function_circumcircle
def circumcircle(a,b,c):
    p = (a+b+c)/2
    R = (a*b*c)/(4*(p*(p-a)*(p-b)*(p-c))**0.5)
    S_1 = (math.pi)*(R**2)
    print(R)
    print(S_1)
#def_function_incircle
def incircle(a,b,c):
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    r = S/p
    S_2 = (math.pi)*(r**2)
    print(r)
    print(S_2)
#input
a_1 = input("a=")
b_1 = input("b=")
c_1 = input("c=")
#processing
a = float(a_1)
b = float(b_1)
c = float(c_1)
#calculation
area(a,b,c)
angle(a,b,c)
circumcircle(a,b,c)
incircle(a,b,c)


#7
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