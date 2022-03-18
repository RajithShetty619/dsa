from multiprocessing.connection import answer_challenge


def pow(x,n):
    ans = 1
    nn =n
    if(n<0):
        nn=-1*n
    while(nn>0):
        if(nn%2!=0):
            nn-=1
            ans=ans*x
        else:
            nn/=2
            x=x*x

    print(ans)

pow(2,10)