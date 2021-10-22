import sys
a = list(map( int, input().split()))
def dec(f):
    def new_f(a):
        if f(a)==0:
            x="Нет("
        elif f(a)>10:
            x="Очень много"
        return (x)
    return new_f
@dec
def chet(a):
    k=0
    for i in range(len(a)):
        if a[i]%2==0:
            k+=1
        return (k)
print(chet(a))
