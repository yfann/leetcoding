def merge(a,b):
    m=len(a)-1
    n=len(b)-1
    a.extend(b)
    k=len(a)-1
    for i in range(k,-1,-1):
        if m>=0 and n>=0:
            if a[m]>b[n]:
                a[i]=a[m]
                m-=1
            else:
                a[i]=b[n]
                n-=1
        elif m>=0:
            a[i]=a[m]
            m-=1
        elif n>=0:
            a[i]=b[n]
            n-=1

    print(a)

