def palindrom(a):
    if len(a)<=1:
        return True
    else :
        if a[0]!=a[-1]:
            return False
    return palindrom(a[1:-1])

vvod=input()
final=''
prom=''
for k in range (2, len(vvod)+1):
    for i in range(0, len(vvod)-k):
        j=k
        while j!=0:
            prom+=vvod[i+j]
            print(j)
            print("Промежуточная ", prom)
            j-=1
        if palindrom(prom) and len(prom)>len(final): 
            final=prom
            prom=''
            print("Финал ", final)
        else: 
            prom=''
print(final)