def findMajorityElement(arr, n): 
    count = 0
    majele =-1


    for i in range(0,n):
        if(count==0):
            majele = arr[i]

        if(arr[i]==majele):
            count +=1
        else:
            count -=1


    count =0
    for i in range(0,n):
        if(arr[i]==majele):
            count +=1
    if(count>n//2):
        return majele
    
    return -1