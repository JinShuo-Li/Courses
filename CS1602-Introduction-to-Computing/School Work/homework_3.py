#1
def triangle(a,b,c):
    if a+b>c and abs(a-b)<c:
        if b+c>a and abs(b-c)<a:
            if a+c>b and abs(a-c)<b:
                print("True")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

triangle(a,b,c)

#2
def delta(a,b,c):
    pbs = b**2 - 4*a*c
    if pbs > 0:
        print("2")
        x_1 = (-b + pbs**1/2)/(2*a)
        x_2 = (-b - pbs**1/2)/(2*a)
        print(f"x1 = {x_1}, x2 = {x_2}")
    elif pbs == 0:
        print("1")
        print(f"x = {-b/(2*a)}")
    else:
        print("0")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta(a,b,c)

#3
def prime(n):
    i = 2
    if n <= 2:
        print("True")
    else:
        while n%i != 0:
            i += 1
        if i == n:
            print("True")
        else:
            print("False")

n = int(input("n = "))
prime(n)

#4
def p_year(y):
    if 1000<=y<10000:
        th4 = y//1000
        hu4 = (y//100)%10
        te4 = (y//10)%10
        un4 = y%10
        if th4 == un4 and hu4 == te4 :
            print("True")
        else:
            print("False")
    elif 100<=y<1000:
        hu3 = y//100
        un3 = y%10
        if hu3 == un3 :
            print("True")
        else:
            print("False")
    elif 10<=y<100:
        if y%11 == 0 :
            print("True")
        else:
            print("False")
    else:
        print("True")

y = abs(int(input("year = ")))
p_year(y)

#5
import math
def f(x):
    if x<-2:
        f = x**4
    elif -2<=x<2:
        f = math.sin(x)
    elif x == 2:
        f = "error"
    else:
        f = math.exp(x)
    return f

x = float(input("x="))
result = f(x)
print(result)

#6
while True:
    x = int(input("x = "))
    if x == 0:
        break
    elif x == -1:
        continue
    else:
        rever_x = str(x)[::-1]
        print(rever_x)
    
#7
n = int(input("n = "))
i = 0
while n%10 == 0:
    n //= 10
    i += 1
print(i)

#8
a = int(input("a = "))
b = int(input("b = "))

def hamming(a: int, b: int):
	return (a ^ b).bit_count()

t = hamming(a,b)
print(t)

#9_1
def is_valid(n):
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return n

n = int(input("n = "))
print(is_valid(n)==1)

#9_2
def is_valid(n):
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return n
for i in range(1,(10**6)+1):
    if is_valid(i) == True:
        continue
    else:
        print("False")
        quit
print("True")

#10
for i in range (1,100001):
    if i%3 == 2 and i%5 == 3 and i%7 == 2:
        print(i)
    else:
        continue

#11
def fractal(n):
    y = n
    if n == 0:
        y = 1
    else:
        for i in range(1,n):
            y *= i
    return y

def choose(n,k):
    z = int(fractal(n)/((fractal(k)*fractal(n - k))))
    return z

def pascal_triangle(n):
    print("[1]")
    for i in range(1,n):
        list = []
        for j in range(0,i+1):
            list.append(choose(i,j))
        print(list)

n = int(input("n="))
pascal_triangle(n)