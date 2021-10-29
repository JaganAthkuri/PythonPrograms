list1 = [1, 2, 3, 5, 4]
#list1.remove(5)
#for i in range(len(list1)-1):
#    if list1[i] == 5:
#        del list1[i]
#print(list1)

list2 = [2, 3, 7, 3, 9]
#list1.extend(list2)

list3 = []

#print(list1)

for i in list1:
    for j in list2:
        k = i + j
        list3.append(k)
print(list3)

my_list = [1,2,3,4]
count = 0
for _ in my_list:
  count +=1
  print(count)

j = [34, 4, 2, 5, 9]
k = j
print(j)
print(k)
k.append("k")
print(j,k)
j.append(6.8)
print(j,k)

list5 = [1, 3, 1, 4, 5, 4, 8, 1]
rem_dup = list(set(list5))
print(rem_dup)