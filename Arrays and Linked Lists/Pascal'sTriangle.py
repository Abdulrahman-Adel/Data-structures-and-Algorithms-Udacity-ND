pascal_triangle = [[1]]
counter = 1
while counter < 10:
    i = pascal_triangle[-1]
    lis = [1]
    if len(i) == 1:
        lis.append(1)
        pascal_triangle.append(lis)
        continue
    for k in range(0,len(i)):
        if k + 2 > len(i):
            lis.append(i[-1])
        else:
            lis.append(sum(i[k:k+2]))
    pascal_triangle.append(lis)
    counter +=1        
    
    
print(pascal_triangle[4])    