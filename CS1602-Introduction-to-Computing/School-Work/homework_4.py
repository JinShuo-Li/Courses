#1
list = input().split()
a = 0
b = 1
for i in list:
    a += float(i)
    b *= float(i)
print(a)
print(b)

#2
list_1 = input("list 1=").split()
list_2 = input("list 2=").split()
for i in list_1:
    if i in list_2:
        continue
    else:
        for i in list_2:
            if i in list_1:
                continue
            else:
                print("False")
                quit()
print("True")

#3
list_input = []
for i in range(1000,3001):
    if i%2 == 0:
        list_input.append(i)
    else:
        continue

print(list_input)

#4
list_1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
i = 0

while i < len(list_1):
    j = i + 1
    while j < len(list_1):
        if list_1[i] == list_1[j]:
            list_1.pop(j)
        else:
            j += 1
    i += 1

print(list_1)

#5
a = int(input())
if a > 0:
    print(str(a)[::-1])
elif a < 0:
    print(int(str(abs(a))[::-1])*(-1))
else:
    print("0")

#6
list_1 = input().split()
list_2 = input().split()
list_3 = []
for i in range(0,len(list_1)):
    if list_1[i] in list_2:
        list_3.append(list_1[i])
if list_3 == []:
    print(list_3 != [])
    print("no intersection")
else:
    print(list_3)

#7
def print_star(n):
    m = 2*n - 1
    for i in range(1,m+1):
        if i <= 5:
            print("* "*i)
        else:
            print("* "*(10-i))

n = int(input())
print_star(n)

#8
def count_digits(n):
    res = [0] * 10
    s = str(n)
    for char in s:
        res[int(char)] += 1
    return res
n = int(input())
lst = count_digits(n)
print(lst)

#9
def sum_of_two(n):
    a = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            a += 2*(10**(j-1))
    return a

n = int(input("n = "))
sum = sum_of_two(n)
print(sum)

#10
A = []
for i in range(10):
    row = list(range(1,11))
    A.append(row)
for row in A:
    print(row)

print("\n")

B = []
for i in range(1,11):
    row = [i]*10
    B.append(row)
for row in B:
    print(row)

#11
def find_min(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return 1

    peak = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            peak = i
            break
    else:
        return len(arr)

    for i in range(peak, len(arr)-1):
        if arr[i] <= arr[i+1]:
            return "error: No valid split point"
    return peak
lst = list(map(int, input().split()))
find_min(lst)
    
#12
def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]
n = int(input())
lst = eratosthenes(n)
print(lst)