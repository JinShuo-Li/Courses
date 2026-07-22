#1
import time
def find_prime(n):
    time_start = time.time()

    number_pn = 0
    for i in range(1,n):
        j = 2
        while j < i:
            if i % j != 0:
                j += 1
                continue
            else:
                break
        if j == i:
            number_pn += 1
        else:
            continue

    time_end = time.time()
    return time_end-time_start, number_pn

#2
import time
def find_prime(n):
    time_start = time.time()

    number_pn = 1
    for i in range(1,n):
        j = 2
        while j < i and j <= int(i**(1/2)) + 1:
            if i % j != 0:
                j += 1
                continue
            else:
                break
        if j == int((i**(1/2))) + 2:
            number_pn += 1
        else:
            continue

    time_end = time.time()
    return time_end-time_start, number_pn

#3
import time
import math

def find_prime(n):
    time_start = time.time()

    if n < 2:
        time_end = time.time()
        return time_end - time_start, 0
    elif n == 2:
        time_end = time.time()
        return time_end - time_start, 1
    elif n == 3:
        time_end = time.time()
        return time_end - time_start, 2
    elif n <= 5:
        time_end = time.time()
        return time_end - time_start, 3  # 2, 3, 5
    
    number_pn = 2
    index = n // 6
    lst = []
    if index == 0:
        if n >= 5:
            lst.append(5)
    else:
        for k in range(1, index + 1):
            candidate1 = 6 * k - 1
            candidate2 = 6 * k + 1
            
            if candidate1 <= n:
                lst.append(candidate1)
            if candidate2 <= n:
                lst.append(candidate2)
    if n >= 5 and 5 not in lst:
        lst.append(5)
    for i in lst:
        is_prime = True
        sqrt_i = int(math.isqrt(i)) + 1
        
        j = 2
        while j < sqrt_i:
            if i % j == 0:
                is_prime = False
                break
            j += 1
        
        if is_prime:
            number_pn += 1
    
    time_end = time.time()
    return time_end - time_start, number_pn

#4
import time

def find_prime(n):
    time_start = time.time()

    if n <= 2:
        time_end = time.time()
        return time_end - time_start, 0
    elif n <= 3:
        time_end = time.time()
        return time_end - time_start, 1
    else:
        number_pn = 0
        judge = [True] * (n-1)
        judge[0] = False
        
        for i in range(1, len(judge)):
            if not judge[i]:
                continue
            number_pn += 1
            k = 2
            while (i+1) * k <= n:
                index_to_mark = (i+1) * k - 1
                if index_to_mark < len(judge):
                    judge[index_to_mark] = False
                k += 1
        
        time_end = time.time()
        return time_end - time_start, number_pn

#5
def Miller_Rabin_test(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    u = n - 1
    t = 0
    while u % 2 == 0:
        u //= 2
        t += 1
    test_bases = [2, 3]
    
    for a in test_bases:
        if a % n == 0:
            continue
        y = pow(a, u, n)
        if y == 1 or y == n - 1:
            continue

        condition_2_satisfied = False
        for _ in range(t - 1):
            y = pow(y, 2, n)
            if y == n - 1:
                condition_2_satisfied = True
                break
            if y == 1:
                return False

        if not condition_2_satisfied and y != n - 1:
            return False
    
    return True

print(Miller_Rabin_test(1000000000000037))
print(Miller_Rabin_test(909091))
print(Miller_Rabin_test(99990001))
print(Miller_Rabin_test(999999000001))
print(Miller_Rabin_test(9999999900000001))
print(Miller_Rabin_test(909090909090909091))
print(Miller_Rabin_test(1111111111111111111))
print(Miller_Rabin_test(11111111111111111111111))
print(Miller_Rabin_test(900900900900990990990991))