//https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1#

int Lpartition(int arr[],int l,int r,int pv)
   {
       swap(arr[pv],arr[r]);
       int pivot=arr[r],i=l-1;
       for(int j=l;j<=r-1;j++)   //Not included lastEle because it's pivot
       {
           if(arr[j]<pivot)
           {
               i++;
               swap(arr[i],arr[j]);
           }
       }
       swap(arr[i+1],arr[r]);
       return (i+1);
   }
   int kthSmallest(int arr[], int l, int r, int k)
   {
       while(l<=r)
       {
           srand(time(NULL));
           int p;
           if(l!=r)
           {
               int range=r-l;
               int pv=(rand()%range)+l; //For getting pivot in range [l,r]
               p=Lpartition(arr,l,r,pv);
           }
           else
           {
               int pv=r;
               p=Lpartition(arr,l,r,pv);
           }
           if(p==k-1)
               return arr[p];
           else if(p>k-1)
               r=p-1;
           else
               l=p+1;
       }
       return -1;
   }