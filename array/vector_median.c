 	 int n = v.size();
     sort(v.begin(), v.end());
     // if even number of elements, mean of middle 2 elements. 
     if(n%2==0) {
      	return (v[n/2-1]+v[n/2])/2;
     }
     // else return the middle element. 
     return v[n/2];