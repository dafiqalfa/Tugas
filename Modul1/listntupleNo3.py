l1 = [2, 4, 3]
l2 = [5, 6, 4]
x, y = '', ''

for i in l1[::-1]:
    x += str(i)

for j in l2[::-1]:
    y += str(j)

z = int(x) + int(y)
keStr = str(z)
keList = list(keStr)
keList.reverse()
print(keList)