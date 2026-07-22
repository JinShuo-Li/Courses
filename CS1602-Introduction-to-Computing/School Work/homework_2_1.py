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