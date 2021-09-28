long long maxSubarraySum(int arr[], int n){
        long long ans=arr[0];
        long long currmax=arr[0]; 
        int i;
        for(i=1;i<n;i++){
            currmax=max(currmax+arr[i],(long long)arr[i]);
            ans=max(ans,currmax);
        }
        return ans;
        
    }