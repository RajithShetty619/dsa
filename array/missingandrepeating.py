def missingAndRepeating(arr, n):
    # Write your code here
 
    duplicate=[0 for i in range(0,n+1)]
    repeating=0
    missing=0
    for i in range(0,n):
        ele=arr[i] 
        if(duplicate[ele] == 1):
            repeating = ele
        else:
            duplicate[ele]=1

    for i in range(1,n+1):
        if(duplicate[i] == 0):
            missing = i

    return [missing,repeating]



print(missingAndRepeating([1,3,5,4,4],5))