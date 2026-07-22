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
