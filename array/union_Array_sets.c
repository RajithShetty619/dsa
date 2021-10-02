class Solution{
    public:
    //Function to return the count of number of elements in union of two arrays.
    int doUnion(int a[], int n, int b[], int m)  {
        //code here
       set<int> v;
       for(int i=0; i<n; i++){
           v.insert(a[i]);
       }
       for(int i=0; i<m; i++){
           v.insert(b[i]);
       }
       int count=0;
       for(auto s:v){
           count++;
       }
       
       return count;
    }
};