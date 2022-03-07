def ninjaAndSortedArrays(arr1,arr2,m,n):
 
    n1pt=0
    n2pt=0
    temp=[]
    while(n1pt<m and n2pt<n):
        if(arr1[n1pt]<arr2[n2pt]):
            temp.append(arr1[n1pt])
            n1pt+=1
        else:
            temp.append(arr2[n2pt])
            n2pt+=1

    while(n1pt<m):
        temp.append(arr1[n1pt])
        n1pt+=1

    while(n2pt<n):
        temp.append(arr2[n2pt])
        n2pt+=1

    return temp

print(ninjaAndSortedArrays([3,6,9,0,0],[4,10],3,2))