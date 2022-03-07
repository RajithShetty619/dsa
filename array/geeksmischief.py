class Solution:
     
    def higher(self, n, arr ,temp_arr):
        if(len(arr)<1):
            return -1
        for i in range(len(arr)):
            if(temp_arr[n] == arr[i]-1): 
                return i
        return -1
    
    
    def lower( self,n,arr,temp_arr):
        if(len(arr)<1):
            return -1
        for i in range(len(arr)):
            if(temp_arr[n] == arr[i]+1): 
                return i
        return -1
    
    def task(self,n,arr,temp_arr,size,correct):
        if(temp_arr==[]):
            temp_arr.append(arr.pop(0))
            self.task(1,arr,temp_arr,size,correct)
            return correct
        else:  
            if(n>size-1):
                if(temp_arr[0]==temp_arr[len(temp_arr)-1]+1):
                    correct.append(temp_arr)
            else:
                low=self.lower(len(temp_arr)-1,arr,temp_arr)
                high=self.higher(len(temp_arr)-1,arr,temp_arr)
                if(low>-1):
                    arr_low=arr
                    temp_arr_low=temp_arr
                    temp_arr_low.append(arr_low.pop(low))
                    self.task(n+1,arr_low,temp_arr,size,correct)
                if(high>-1):
                    arr_high=arr
                    temp_arr_high=temp_arr
                    temp_arr_high.append(arr_high.pop(high))
                    self.task(n+1,arr_high,temp_arr,size,correct)
       
    def completeTask (self, N, arr):
        # code here 
        arr.sort() 
        temp = arr[N-1]
        for i in range(N-1,0,-1):
            arr[i]=arr[i-1]  
        arr[0]=temp 
        correct = []
        correct = self.task(0,arr,[],N,correct)
        if(len(correct)>0):
            print("YES")
        else:
            print("NO")

print(Solution().completeTask(6,[1, 1, 2, 2, 2, 3]))