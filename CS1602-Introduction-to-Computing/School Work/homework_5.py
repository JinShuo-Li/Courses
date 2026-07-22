#1
b = input().split()
a = [int(t) for t in b]
for i in range(0,len(a)):
    j = i+1
    while j<=len(a)-1:
        if a[i] == a[j]:
            a.pop(j)
        else:
            j += 1
a.sort()
print(list(reversed(a)))

#2
a = input().split()
for i in range(0,len(a)):
    a[i] = a[i].upper()
print(a)

#2'试图一行实现
print([word.upper() for word in input().split()])

#3
a_inp = input().split()
b_inp = input().split()
a = [int(t) for t in a_inp]
b = [int(k) for k in b_inp]
c = a + b
c.sort()
print(c)

#4
a_inp = input().split()
a = [int(i) for i in a_inp]
e = 0
o = 0
for j in a:
    if j%2 == 0:
        e += 1
    else:
        o += 1
print(f"the number of even numbers is {e}")
print(f"the number of odd numbers is {o}")

#5
def is_valid(password):
    if len(password) < 6 or len(password) > 16:
        return False
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in ["$","#","@"]:
            has_special = True

    return has_lower and has_upper and has_digit and has_special

password = input()
judge = is_valid(password)
print(judge)

#6
a = input()
b = a.upper()
lst = ["A","E","I","O","U"]
if b in lst:
    print("vowel")
else:
    print("consonant")

#7
dic = {"january":31,
       "february":28,
       "march":31,
       "april":30,
       "may":31,
       "june":30,
       "july":31,
       "august":31,
       "september":30,
       "october":31,
       "novermber":30,
       "december":31}
a = input()
a_lower = a.lower()
print(dic[a_lower])

#8
a = input()
print(a.isnumeric())

#9
a = int(input())
_ = int(input())
if 1<=a<=3:
    print("Q1")
elif 4<=a<=6:
    print("Q2")
elif 7<=a<=9:
    print("Q3")
elif 10<=a<=12:
    print("Q4")

#10
def zodiac(n):
    zodiac_mapping = {
        0: "Rat", 1: "Ox", 2: "Tiger", 3: "Rabbit",
        4: "Dragon", 5: "Snake", 6: "Horse", 7: "Goat",
        8: "Monkey", 9: "Rooster", 10: "Dog", 11: "Pig"}
    index = (n-4)%12
    return zodiac_mapping[index]
a = int(input())
result = zodiac(a)
print(result)

#11
def the_next_date(x,y,z):
    dict1 = {1:31,2:28,3:31,4:30,5:31,6:30,
             7:31,8:31,9:30,10:31,11:30,12:31}
    dict2 = {1:31,2:29,3:31,4:30,5:31,6:30,
             7:31,8:31,9:30,10:31,11:30,12:31}
    if z == 31 and y == 12:
        print(f"{x+1}-1-1")
    elif (x%4 == 0 and x%100 != 0) or x%400 == 0:
        if z == dict2[y]:
            print(f"{x}-{y+1}-1")
        elif z < dict2[y]:
            print(f"{x}-{y}-{z+1}")
        else:
            print("Please check your input, it seems that your input is invalid!")
    else:
        if z == dict1[y]:
            print(f"{x}-{y+1}-1")
        elif z < dict1[y]:
            print(f"{x}-{y}-{z+1}")
        else:
            print("Please check your input, it seems that your input is invalid!")

x = int(input())
y = int(input())
z = int(input())
the_next_date(x,y,z)

#12
def process_speech(speech):
    for char in ("--", ".", ","):
        speech = speech.replace(char, "")
    cleaned_text = speech.lower()
    word_counts = {}
    for word in cleaned_text.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    letter_counts = {}
    for char in cleaned_text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return {
        "Processed Text": cleaned_text,
        "Frequency of words": word_counts,
        "Frequency of letters": letter_counts}
speech = input()
result = process_speech(speech)
print(result)