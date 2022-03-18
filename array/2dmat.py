 
def findTargetInMatrix(mat, m, n, target):
	# Write your code here.
	#let search in m 
    i,j = n-1,m-1
    visited = n 
    while(visited>j and j>=0):
        if(target>=mat[j][0]):
            if(target<=mat[j][i]):
                for k in range(0,n):
                    if(target==mat[j][k]):
                        print("TRUE")
                        return
                break
            else:
                j+=1

        elif(target<mat[j][0]):
            visited = j
            j = j//2
    print("FALSE")
    return 
    
findTargetInMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]],3,4,8)