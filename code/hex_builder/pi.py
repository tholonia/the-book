def iteration(N,h,s,p):
    n=N-(1/s)+(1/p)
    print(n*4)
    iteration(n,h,s+h**2,p+h*2)
iteration(1,2,3,5)
