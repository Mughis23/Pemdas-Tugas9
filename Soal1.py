arr = [8,3,12,4,7,2]

result=[]
for x in arr:
    if x < 5 :
        result.append(0)
    else:
        result.append(x)
        
result.sort(reverse=True)
print("Output nya : ", result)