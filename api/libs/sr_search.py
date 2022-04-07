from time import sleep
from sympy import *
from sympy.solvers import solve


def f(x):
    return pow(x,4) + 2 * pow(x,2) +  4*x

def f_d(y):
    x = Symbol('x') 
    f =  pow(x,4) + 2 * pow(x,2) +  4*x
    df =  f.diff(x)
    result  = df.subs(x, y)
    return result

def algo(a, b,eps):
    n = 0
    while True:
        y = (a+b)/2
        rs = f_d(y)

        if  abs(rs) <= eps:
            return y,n
        else:
            n+=1
            if rs> 0:
                b = y
            elif rs < 0:
                a = y


def solve_algo_sr(a,b,eps):
    x,n = algo(a,b,eps)
    y = f(x)
    result = [x,y,n]
    values  = list(map(lambda x: round(x,len(str(eps))- 2), result))

    return values

