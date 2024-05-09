arr = [105, 20, 8, 150, 30, 5, 200]
result =[]
for x in arr:
    if 10 <= x <= 100:
        result.append(x)
result.sort()
print("Output : ", result)