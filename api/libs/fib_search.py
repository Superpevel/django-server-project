from math import fabs
from optparse import Values
 
def f(x):
    return pow(x,5) - pow(x,2)

def fun(n):
    sum=0
    f1 = 1
    f2 = 1
    m = 0
    while (m < n - 1):
        sum = f1 + f2
        f1 = f2
        f2 = sum
        m+=1
    return f1


def fibanachi(a,b,eps):
    k = 0
    N = 21
    x1 = a + (fun(N - 2) * (b - a) / fun(N))
    x2 = a + (fun(N - 1) * (b - a) / fun(N))
    f1 = f(x1)
    f2 = f(x2)
    while (k !=N-2):
        if (f1 > f2):
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (fun(N - k - 1) * (b - a) / fun(N - k))
            if (k == N - 2):

                x2 = x1 + eps
                if (f(x1) > f(x2)):
                    a = x1
                else:
                    b = x2
            else:
                f2 = f(x1)
                k = k+1
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (fun(N - k - 2) * (b - a) / fun(N - k))
            if (k == N - 2):
                x2 = x1 + eps
                if (f(x1) > f(x2)):
                    a = x1
                    b = x2
            else:
                f1 = f(x1)
                k = k+1

    xmin = (a + b) / 2
    print(f"a = {a}, b={b}, x min = {xmin} , fun {f(xmin)} , k = {k}, N = {N}")
    return [a,f(xmin),k]


def fib_search(a,b,eps):
    result = fibanachi(a,b,eps)
    values  = list(map(lambda x: round(x,len(str(eps))- 2), result))
    return values