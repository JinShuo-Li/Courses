#1
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return f(f(n//2))+1

n = int(input())
print(f(n))

#2
def a(n):
    if n==0 or n==1:
        return 1
    else:
        return a(n-1)+a(n-2)

n = int(input())
print(a(n))

#3
def list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += list_sum(i)
        else:
            total += i
    return total

t = list_sum([1, 2, [3,4], [5,6]])
print(t)

#4
def count(lst):
    list_acc = []
    for i in lst:
        if type(i) == list:
            for j in count(i):
                if j in list_acc:
                    continue
                else:
                    list_acc.append(j)
        else:
            if i not in list_acc:
                list_acc.append(i)
            else:
                continue
    list_ter = sorted(list_acc)
    return list_ter

def times(k,lst):
    t = 0
    for s in lst:
        if type(s) == list:
            t += times(k,s)
        elif s == k:
            t += 1
        else:
            continue
    return t

list_test = [1, 2, 3, 4, 5, 6, [3,4,5,6], [5,6]]
key = count(list_test)
dic = {}
for i in key:
    dic[i] = times(i,list_test)
print(dic)

#5
def Hadamard(k):
    if k == 0:
        return [[1]]
    elif k == 1:
        return [[1,1],[1,-1]]
    else:
        H_prev = Hadamard(k - 1)
        n = len(H_prev)
        H = []
        for i in range(n):
            H.append(H_prev[i] + H_prev[i])
        for i in range(n):
            H.append(H_prev[i] + [-x for x in H_prev[i]])
        return H

k = int(input())
print(Hadamard(k))

#6
def Powerset(S: set) -> list[set]:
    result = [set()]
    
    for element in S:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset | {element})
        result += new_subsets
    return result

print(Powerset({1,2,3}))

#Eight Queen Problem
def is_safe(n,tup):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if abs(tup[j] - tup[i]) == abs(j - i):
                return False
            else:
                continue
    return True

from itertools import  permutations
n = int(input())
a = list(range(1,n+1))
count = 0
storage = []
for i in permutations(a,n):
    if is_safe(n,i):
        count += 1
        storage.append(i)
    else:
        continue

print(count)
print(storage)