def maximumProfit(prices):  
    min =prices[0] 
    profit=0
    for i in range(len(prices)):
        if(i==0):
            min=prices[0] 
        else:
            if(prices[i]-min>profit and min<prices[i]):
                profit=prices[i]-min
            elif(min>prices[i]):
                min=prices[i]
    
     
    return profit

print(maximumProfit([98,101,66,72]))