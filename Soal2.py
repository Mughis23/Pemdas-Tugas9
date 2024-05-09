arr=[7, 4, 9, 2, 5, 1]
genap =[]

for x in arr:
    if x % 2 == 0:
        genap.append(x)
genap.sort()
print("Angka yang di input : ",arr)
print("Angka genap : ",genap)   