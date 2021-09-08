
#doan nay input tu ban phim
m = 3
n = 4
list = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]
# doan nay khai bao bien
list_sorted = []
list2_sorted = []
list3 = []
list4 = []
list5 = []
for row in list: #tung element trong list se duoc sap xep theo chan le, sap xep theo chan le de gop le vao 1  cot
    row2 = sorted(row,key=lambda x:x%2!=0)
    list_sorted.append(row2)
#print(list_sorted)

list2 = [x for x in zip(*list_sorted)] #chia cai vua xep ra thanh nhung cot, va don nhung phan tu trong cot vao 1 list
#print(list2)

for row in list2: # xet tung element(bay gio la cot) trong list 2
    if row[0]%2 != 0: # neu la so le thi xep tu lon den be, chan nguoc lai
        row2 = sorted(row,reverse=True)
        list2_sorted.append(row2)
    else: list2_sorted.append(row) #chen vao list khac

for el in list2_sorted: #chia list2_sorted thanh 2 list, 1 list giu so chan, 1 list giu so le
    if el[0]%2 !=0:
        list3.append(el)
    else: list4.append(el)
list3 = sorted(list3,reverse=True) #sort lai list le, sao cho so lon dung truoc trong cot

#print ra theo yeu cau
for x,y in zip(list3,list4):
    list5.append(x)
    list5.append(y)
print(list5) #
for i in range(0,m):
    for j in range(0,n):
        print(list5[j][i],end=" ")
        if j == n-1: print()
