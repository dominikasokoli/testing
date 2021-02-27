def f1(a, b=0):
    return a*a+b

def f2(a):
    if len(a)==0:
        return "BUUM"
    else:
        return a[0]
def f3(a):
    if a==1:
        return "jeden"
    elif a==2:
        return "dwa"
    elif a==3:
        return "trzy"
    elif a>4 and a<1000:
        return "other"

def f4(a, b=666):
    if b==666:
        return "%s ma kota" %a
    else:
        return "%s ma kota i %s" %(a,b)
def f5(c, d=1):
    return list(range(c))[::d]
