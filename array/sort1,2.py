def sortColors(nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one =0
        two =0
        
        for i in range(len(nums)):
            if(nums[i]==0):
                zero=zero+1
            if(nums[i]==1):
                one=one+1
            if(nums[i]==2):
                two=two+1
        nums.clear()
        while(zero>0):
            nums.append(0)
            zero=zero-1
        while(one>0):
            nums.append(1)
            one=one-1
        while(two>0):
            nums.append(2)
            two=two-1
        return nums

print(sortColors([2,0,2,1,1,0]))