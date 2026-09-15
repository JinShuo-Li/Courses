#1
def isvalid_hp_num(n,check=None):
    if check is None:
        check = []
    sum_var = 0
    if n == 1:
        return True
    elif n in check:
        return False
    check.append(n)
    for i in str(n):
        sum_var += (int(i))**2
    return isvalid_hp_num(sum_var,check)
#What we have learned: In recursion if we want to have an object inherited from the last recursion, add it in to the "input" or "variants" section, and add a default setting.

#2
def find_prime(n):
    if n <= 2:
        return 0
    elif n <= 3:
        return 1
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
        return number_pn
#What we have learned: A good method is better than great calculation in many cases. Use mathematics.

#3
#Assume str_s and str_t have the same length.
def isvalid_iso_strings(str_s, str_t):
    lst1 = list(str_s)
    lst2 = list(str_t)
    lst_assis = [False]*(len(str_s))
    for i in range(len(str_s)):
        if lst_assis[i] == False:
            lst_location = []
            for j in range(i,len(str_s)):
                if lst1[j] == lst1[i]:
                    lst_location.append(j)
            for k in lst_location:
                if lst2[lst_location[0]] == lst2[k]:
                    lst_assis[k] == True
                else:
                    return False
    return True
#What we have learned: Use boolean list to make the program runs more effectively.

#4
def isvalid_duplicate(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] == lst[i]:
                return True
    else:
        return False
#What we have learned: Mind the index when searching through the list

#5_1
def isvalid_duplicate_distance(lst,k):
    for i in range(len(lst)):
        if i-k < 0:
            min_ = 0
        else:
            min_ = i-k
        if i+k > len(lst):
            max_ = len(lst)
        else:
            max_ = i+k
        for j in range(min_,max_):
            if lst[i] == lst[j] and i != j:
                return True
    else:
        return False
#What we have learned: Mind the indices.

#5_2
def isvalid_duplicate_distance_hash(lst,k):
    last_seen = {}
    for i, num in enumerate(lst):
        if num in last_seen:
            if abs(i-last_seen[num]) <= k:
                return True
        last_seen[num] = i
    return False
#What we have learned: Hash table(The enumerate function) can make the calculation more faster.

#6
def is_power_of_two_rec(n):
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    else:
        return is_power_of_two_rec(n//2)
#What we have learned: The recursion can be effective.

#7
def is_valid_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    lst1 = list(str1)
    lst2 = list(str2)
    for i in range(len(lst1)):
        if lst1[i] in lst2 and lst1.count(lst1[i]) == lst2.count(lst1[i]):
            continue
        else:
            return False
    return True

#8_1
def add_digits(n):
    n_str = str(n)
    while len(n_str) > 1:
        sum_digits = 0
        for i in n_str:
            sum_digits += int(i)
        n_str = str(sum_digits)
    return str(n_str)

#8_2 (O(1) simplified)
def add_digits_sim(n):
    if n == 0:
        return 0
    elif n % 9 == 0:
        return 9
    else:
        return n % 9

#9
def is_valid_ugly_number(n):
    if n == 1:
        return True
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5
    if n != 1:
        return False
    else:
        return True

#10_1
def find_missing_number(lst):
    lst_ref = list(i for i in range(len(lst)+1))
    for i in lst_ref:
        if i not in lst:
            return i
        else:
            continue
    return None

#10_2 (O(n) O(1) simplified)
def find_missing_number_sim(lst):
    n = len(lst)
    total = n * (n+1)/2
    actual_sum = sum(lst)
    return int(total-actual_sum)

#11
def move_zeroes(array):
    if not isinstance(array,list):
        raise TypeError
    lenth = len(array)
    counter = 0
    assis = 0
    index = 0
    while index < lenth:
        if array[index - assis] != 0:
            index += 1
        else:
            array.pop(index - assis)
            assis += 1
            counter += 1
            index += 1
    empty = [0 for _ in range(counter)]
    res = array + empty
    return res

#12
def pattern_match(pattern, str):
    pattern_lst = []
    for i in pattern:
        pattern_lst.append(i)
    str_lst = str.split()
    if len(str_lst) != len(pattern_lst):
        return False
    else:
        boolean_lst = [False for _ in range(len(pattern_lst))]
        for i in range(len(str_lst)):
            if boolean_lst[i] == False:
                for j in range(i,len(pattern_lst)):
                    if (pattern_lst[i] == pattern_lst[j] and str_lst[i] == str_lst[j]) or (pattern_lst[i] != pattern_lst[j] and str_lst[i] != str_lst[j]):
                        boolean_lst[j] = True
                    else:
                        return False
            else:
                continue
        return True

#13
def nim_game(n):
    if n <= 3:
        return True
    if n == 4:
        return False
    else:
        for i in range(1,4):
            if not nim_game(n-i):
                return True
        return False

#14_1
def is_pow_of_tri(n):
    while True:
        if n % 3 == 0:
            n //= 3
        elif n == 1:
            return True
        else:
            return False

#14_2
def is_pow_of_tri_sim(n):
    return n > 0 and 1162261467 % n == 0

#15
def is_pow_of_fort(n):
    while True:
        if n % 4 == 0:
            n //= 4
        elif n == 1:
            return True
        else:
            return False

#16
def rev(string):
    res = []
    for i in string:
        res.append(i)
    res.reverse()
    return ''.join(res)

#17
def rev_vowel(string):
    vowel = ['A','a','E','e','I','i','O','o','U','u']
    lst1 = []
    lst2 = []
    assis = []
    for i in range(len(string)):
        assis.append(string[i])
        if string[i] in vowel:
            lst1.append(i)
            lst2.append(string[i])
    lst2.reverse()
    for j in range(len(lst1)):
        assis[lst1[j]] = lst2[j]
    return ''.join(assis)

#18
def find_intersec(lst1,lst2):
    if len(lst1) > len(lst2):
        lst1,lst2 = lst2,lst1
    intersec = []
    for i in lst1:
        if i in intersec:
            continue
        else:
            if i in lst2:
                intersec.append(i)
    return intersec

#19
def find_intersec_com(lst1,lst2):
    if len(lst1) > len(lst2):
        lst1,lst2 = lst2,lst1
    intersec = []
    for i in lst1:
        if i in lst2:
            intersec.append(i)
    return intersec

#20
def is_perfect_square(num):
    if num == 1 or num == 4:
        return True
    else:
        for i in range(2,int(num/2+1)):
            if num / i == i:
                return True
            else:
                continue
        return False
    
#21
def is_valid_ransom_note(ransom,maga):
    if (not isinstance(ransom,str)) or (not isinstance(maga, str)):
        raise TypeError
    if len(ransom) < len(maga):
        return False
    lst_ransom = list(ransom)
    lst_maga = list(maga)
    for i in lst_ransom:
        if i in lst_maga:
            lst_maga.remove(i)
        else:
            return False
    return True

#22
def index_first_unique_chr(string):
    for i in range(len(string)):
        assis = list(string)
        assis.pop(i)
        if string[i] in assis:
            continue
        else:
            return i
    return -1

#23
def find_diff(string1, string2):
    lst1 = list(string1)
    lst2 = list(string2)
    for i in lst1:
        if i not in lst2:
            return i
        else:
            lst2.remove(i)
    raise ValueError

#24
def find_digits(n):
    t = 1
    lst = []
    while len(lst) <= n:
        new_lst = list(str(t))
        lst += new_lst
        t += 1
    return lst[n-1]

#25
def count_palindrome(string):
    rec = []
    dic = dict()
    for i in string:
        count = 0
        if i in rec:
            continue
        for j in string:
            if i == j:
                count += 1
            else:
                continue
        dic[i] = count
    odd = []
    eve = []
    for key in dic:
        if dic[key] % 2 != 0:
            odd.append(dic[key])
        else:
            eve.append(dic[key])
    return max(odd) + sum(eve)

#26
def thirdMax(nums):
    first = second = third = None
    for num in nums:
        if num == first or num == second or num == third:
            continue
        if first is None or num > first:
            third = second
            second = first
            first = num
        elif second is None or num > second:
            third = second
            second = num
        elif third is None or num > third:
            third = num
    return third if third is not None else first

#27
def count_segments(string):
    counter = 0
    for i in range(len(string)):
        if i == len(string) - 1:
            if string[i] == " " and string[i-1] == " ":
                pass
            else:
                counter += 1
        else:
            if string[i] == " " and string[i-1] != " ":
                counter += 1
            else:
                pass
    return counter

#28
def findAnagrams(s, p):
    if len(s) < len(p):
        return []
    
    result = []
    p_count = [0] * 26
    for ch in p:
        p_count[ord(ch) - 97] += 1
    window_count = [0] * 26

    for i in range(len(p)):
        window_count[ord(s[i]) - 97] += 1
    if window_count == p_count:
        result.append(0)
    for i in range(len(p), len(s)):
        left_char_index = ord(s[i - len(p)]) - 97
        window_count[left_char_index] -= 1
        right_char_index = ord(s[i]) - 97
        window_count[right_char_index] += 1
        if window_count == p_count:
            result.append(i - len(p) + 1)
    return result

#29
def arrange_coins(n):
    sum = 0
    clock = 1
    while sum < n:
        sum += clock
        clock += 1
    remain = sum - n
    clock -= 1
    if remain != 0:
        clock -= 1
    return clock

#30
def string_compression(lst):
    i = 0
    res = []
    while i < len(lst) -1:
        if lst[i] == lst[i+1]:
            j = 1
            while i + j + 1 < len(lst) and lst[i+j] == lst[i+j+1]:
                j += 1
            j += 1
            index = list(str(j))
            res.append(lst[i])
            res += index
            i += j
        else:
            res.append(lst[i])
            i += 1
    return res

#31
def find_disappeared_nums(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    return res

#32
def find_min_moves(lst):
    return sum(lst) - min(lst)*len(lst)

#33
def assign_cookies(lst1, lst2):
    lst1.sort()
    lst2.sort()
    counter = 0
    i,j = 0,0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            counter += 1
            i+=1
            j+=1
        else:
            j += 1
    return counter

#34
def find_pattern(string):
    for index in range(1, len(string)//2+1):
        if len(string) % index != 0:
            continue
        else:
            is_valid = True
            for i in range(index,len(string)):
                if string[i] != string[i % index]:
                    is_valid = False
                    break
    if is_valid:
        return True
    else:
        return False

#35
def hamm_distance(m,n):
    str1 = list(str(bin(m)))
    str2 = list(str(bin(n)))
    for i in range(2):
        str1.pop(0)
        str2.pop(0)
    zeros = ['0' for _ in range(abs(len(str1)-len(str2)))]
    if len(str1)<len(str2):
        str1 = zeros + str1
    else:
        str2 = zeros + str2
    res = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            res += 1
    return res

#36
def heaters(lst1,lst2):
    check = [False for _ in lst1]
    maxium = max(lst1)
    radius = 1
    while False in check and radius <= maxium:
        ran = []
        for i in lst2:
            for j in range(-1*radius, radius+1):
                ran.append(i+j)
        for k in range(len(lst1)):
            if lst1[k] in ran:
                check[k] = True
            else:
                radius += 1
                break
        else:
            return radius
    return None

#37
def num_complement(n):
    binary = bin(n)[2:]
    res = int(''.join('1' if bit == '0' else '0' for bit in binary), 2)
    return res

#37_sim
def num_complement_sim(n):
    mask = (1 << n.bit_length()) - 1
    return n ^ mask
#Powerful bit operations!

#38
def largest_palin_prod(n):
    def is_palin(m):
        s = str(m)
        return s == s[::-1]
    max_num = 10**n-1
    min_num = 10**(n-1)
    res = 0
    for i in range(max_num,min_num-1,-1):
        for j in range(i,min_num-1,-1):
            product = i*j
            if product <= res:
                break
            if is_palin(product):
                res = max(res, product)
    return res

#39
def formating(string, k):
    clean_str = ''.join(string.split('-')).upper()
    first_group_len = len(clean_str) % k
    if first_group_len == 0:
        first_group_len = k
    result = clean_str[:first_group_len]
    for i in range(first_group_len, len(clean_str), k):
        result += '-' + clean_str[i:i+k]
    return result

#40
def max_consecutive_ones(lst):
    counter = 0
    largest = 0
    while counter < len(lst):
        if lst[counter] != 1 or lst[counter] != lst[counter+1]:
            counter += 1
            continue
        else:
            index = 1
            while counter + index < len(lst) and lst[counter] == lst[counter+index]:
                index += 1
            largest = max(largest,index)
            counter += index
    return largest

#41
def next_greater_e(nums1, nums2):
    res = []
    for i in nums1:
        index = nums2.index(i)
        for j in range(index+1,len(nums2)):
            if i < nums2[j]:
                res.append(nums2[j])
                break
            else:
                continue
        else:
            res.append(-1)
    return res

#42
def perfect_num(n):
    total = 0
    for i in range(1, int(n/2+1)):
        if n % i == 0:
            total += i
    if n == total:
        return True
    else:
        return False
    
#43
import math
def maximum_prod(lst):
    ma1, ma2, ma3, mi1, mi2 = -1001,-1001,-1001,1001,1001
    for i in lst:
        if i > ma1:
            ma3 = ma2
            ma2 = ma1
            ma1 = i
        elif i > ma2:
            ma3 = ma2
            ma2 = i
        elif i > ma3:
            ma3 = i
        if i < mi1:
            mi2 = mi1
            mi1 = i
        elif i < mi2:
            mi2 = i
    if ma1 < 0 or ma3 > 0:
        return ma1*ma2*ma3
    else:
        return mi1*mi2*ma1
    
#44
def sum_of_square_nums(n):
    sum = 0
    index = 1
    while sum < n:
        sum += index**2
        index += 1
    if sum == n:
        return True
    else:
        return False
