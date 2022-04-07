 
def f(x):
    return pow(x,5) - pow(x,2)
 


def div_search(a,b,eps):
    n = 0
    x = (a + b) / 2
    sig = eps/2 - 0.000000000001
    while ((b - a) >= eps):
        n+=1
        x1  = (a + b) / 2 - sig
        x2  = (a + b) / 2 + sig
        f1 = f(x1)
        f2 = f(x2)
        if f1<f2:
            b = x2
        else:
            a = x1

    return a,b,n

def dv_search(a,b,eps):
    result = div_search(a, b, eps)
    values  = list(map(lambda x: round(x,len(str(eps))- 2), result))
    return values
