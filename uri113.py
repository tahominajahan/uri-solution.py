area=input().split(" ")
a,b,c=area
a=int(a)
b=int(b)
c=int(c)
F=(a+b+abs(a-b))/2
K=(b+c+abs(b-c))/2
U=(F+K+abs(F-K))/2
print(int(U),"eh o maior")