'''l1 = [0,1,2,3,4,5]
l2=[1]

l2.append(l1[0]+l1[5])
print(l1[0]+l1[5])
print(l2)
l2.append(l1[1]+l1[4])
print(l2)
l2.append(l1[2]+l1[3])
print(l2)
l2.pop(0)
print(l2)'''
lst = [0, 1, 2, 3, 4, 5]

list2 = []

for i in range(0,(len(lst)//2)):

    x = lst[i-1] + lst[-i]

    list2.append(int(x))

print(list2)


#print(l1[1]+l1[4])
