#####list_lasted
#list_comprehention
print([x**2 for x in range(1,11) if x%2 == 0])
print([x**2 for x in range(1,11)])

#nested_comprehension
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print([[row[i] for row in matrix] for i in range(4)])

#built-in function
list_test = [2,1,3,4]
#-len
print(len(list_test))
#-min/max
print(min(list_test),max(list_test))
#-sum
print(sum(list_test))
#-sorted
print(sorted(list_test))
#-reversed
print(list(reversed(list_test)))
print("".join(str(x)for x in list_test),end="")

#emurate
lst = [1,2,3,4]
for i,_ in enumerate(lst):
    print(i,_)

#####dictionary
#merge: the last one will cover the first one if they shared the same keywords.
a = {1:0,2:1,3:2,4:3}
b = {1:1,2:1,3:2}
c = {**a,**b}
print(c)

#loop through dictionaries
dictionary = {1:0,2:1,3:2,4:3}
for x in dictionary:
    print(x)
for x in dictionary:
    print(dictionary[x])
for x in dictionary.values():
    print(x)
for x,y in dictionary.items():
    print(x,y)

#upper函数不会自动修改，而是返回修改值
#lst.sort不会返回修改值，而是自动修改