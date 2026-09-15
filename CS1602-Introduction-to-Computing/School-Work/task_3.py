def remove_leading_zeros(s: str) -> str:
    i = 0
    while i < len(s) - 1 and s[i] == '0':
        i += 1
    return s[i:]


def compare_abs(str1: str, str2: str) -> int:
    str1 = remove_leading_zeros(str1)
    str2 = remove_leading_zeros(str2)
    
    len1, len2 = len(str1), len(str2)
    if len1 > len2:
        return 1
    elif len1 < len2:
        return -1
    
    for i in range(len1):
        if str1[i] > str2[i]:
            return 1
        elif str1[i] < str2[i]:
            return -1
    return 0


def add_abs(str1: str, str2: str) -> str:
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    str1 = str1[::-1]
    str2 = str2[::-1]
    
    result = []
    carry = 0
    
    for i in range(len(str1)):
        digit1 = int(str1[i])
        digit2 = int(str2[i]) if i < len(str2) else 0
        
        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10
    
    if carry:
        result.append(str(carry))
    
    return remove_leading_zeros(''.join(result[::-1]))


def sub_abs(str1: str, str2: str) -> str:
    if compare_abs(str1, str2) == 0:
        return "0"
    
    str1 = str1[::-1]
    str2 = str2[::-1]
    
    result = []
    borrow = 0
    
    for i in range(len(str1)):
        digit1 = int(str1[i]) - borrow
        digit2 = int(str2[i]) if i < len(str2) else 0
        
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        
        result.append(str(digit1 - digit2))

    res = remove_leading_zeros(''.join(result[::-1]))
    return res


def mul_abs(str1: str, str2: str) -> str:
    if str1 == "0" or str2 == "0":
        return "0"
    
    len1, len2 = len(str1), len(str2)
    result = [0] * (len1 + len2)
    
    str1 = str1[::-1]
    str2 = str2[::-1]
    
    for i in range(len1):
        for j in range(len2):
            mul = int(str1[i]) * int(str2[j])
            pos = i + j
            result[pos] += mul
            result[pos + 1] += result[pos] // 10
            result[pos] %= 10
    
    res_str = ''.join(str(digit) for digit in result[::-1])
    return remove_leading_zeros(res_str)


def div_abs(dividend: str, divisor: str):
    if divisor == "0":
        raise ZeroDivisionError
    
    if compare_abs(dividend, divisor) < 0:
        return "0", dividend
    
    quotient = []
    remainder = 0
    index = 0
    n = len(dividend)
    
    while index < n:
        current = remainder * 10 + int(dividend[index])
        index += 1
        
        if current < int(divisor):
            quotient.append("0")
        else:
            q = current // int(divisor)
            quotient.append(str(q))
            remainder = current % int(divisor)
        
        remainder = current % int(divisor)
    
    if not quotient:
        quotient.append("0")
    
    q_str = remove_leading_zeros(''.join(quotient))
    r_str = str(remainder)
    
    return q_str, r_str


def add(str1: str, str2: str) -> str:

    sign1 = str1[0] if str1[0] in '+-' else '+'
    sign2 = str2[0] if str2[0] in '+-' else '+'
    
    num1 = str1[1:] if str1[0] in '+-' else str1
    num2 = str2[1:] if str2[0] in '+-' else str2
    
    num1 = remove_leading_zeros(num1)
    num2 = remove_leading_zeros(num2)

    if num1 == "0" and num2 == "0":
        return "0"
    if num1 == "0":
        return str2
    if num2 == "0":
        return str1

    if sign1 == sign2:
        result = add_abs(num1, num2)
        return ("-" if sign1 == '-' else "") + result

    cmp = compare_abs(num1, num2)
    if cmp == 0:
        return "0"
    elif cmp > 0:
        result = sub_abs(num1, num2)
        return ("-" if sign1 == '-' else "") + result
    else:
        result = sub_abs(num2, num1)
        return ("-" if sign2 == '-' else "") + result


def sub(str1: str, str2: str) -> str:
    if str2[0] == '-':
        new_str2 = str2[1:]
    elif str2[0] == '+':
        new_str2 = '-' + str2[1:]
    else:
        new_str2 = '-' + str2
    
    return add(str1, new_str2)


def mul(str1: str, str2: str) -> str:
    sign1 = str1[0] if str1[0] in '+-' else '+'
    sign2 = str2[0] if str2[0] in '+-' else '+'
    
    num1 = str1[1:] if str1[0] in '+-' else str1
    num2 = str2[1:] if str2[0] in '+-' else str2

    num1 = remove_leading_zeros(num1)
    num2 = remove_leading_zeros(num2)

    if num1 == "0" or num2 == "0":
        return "0"

    result = mul_abs(num1, num2)

    if sign1 == sign2:
        return result
    else:
        return '-' + result


def div(str1: str, str2: str):

    num1 = remove_leading_zeros(str1)
    num2 = remove_leading_zeros(str2)
    
    if num2 == "0":
        raise ZeroDivisionError
    
    return div_abs(num1, num2)

def pow(str1: str, n: int) -> str:
    if n == 0:
        return '1'
    if str1 == '0':
        return '0'
    if n == 1:
        return str1
    
    result = '1'
    base = str1
    exp = n
    
    while exp > 0:
        if exp & 1:
            result = mul(result, base)
        base = mul(base, base)
        exp >>= 1
    
    return result

print(add('22222222222222','8773849905050505'))
print(22222222222222+8773849905050505)
print('_____________')
print(sub('11111111','9877344555'))
print(11111111-9877344555)
print('_____________')
print(sub('345676778778','222222'))
print(345676778778-222222)
print('_____________')
print(div('8773849905050505','123'))
print(8773849905050505//123)
print(8773849905050505%123)
print('_____________')
print(pow('123456',789))
print(123456**789)