 

from sys import stdin,setrecursionlimit,maxsize

setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    currmax=0
    prevmax=0
    ans=0
    for i in range(n):
        if(i==0):
            currmax=arr[0]
        else:
            currmax=max(prevmax+arr[i],arr[i])
        prevmax=currmax
        ans=max(currmax,ans) 
    return ans
     
