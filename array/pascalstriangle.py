def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    
    pascallist =[[1]]
    for i in range(n-1):
        templist1=[1]
        for j in range(1,i+1):  
                templist1.append(pascallist[i][j-1]+pascallist[i][j]) 
        templist1.append(1) 
        pascallist.append(templist1)
    return pascallist
             
        
print(printPascal(4))