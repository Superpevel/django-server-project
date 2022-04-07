from time import sleep
from sympy import im
from sympy import *

import math


def f(x):
    return pow(x,4) + 2 * pow(x,2) +  4*x

def f_dd(y):
    x = Symbol('x') 
    f =  pow(x,4) + 2 * pow(x,2) +  4*x
    df =  f.diff(x)
    df = df.diff(x)
    result  = df.subs(x, y)
    return result
 

def f_d(y):
    x = Symbol('x') 
    f =  pow(x,4) + 2 * pow(x,2) +  4*x
    df =  f.diff(x)
    result  = df.subs(x, y)
    return result


def search(a,b,eps):

    k = 0
    x = (a+b)/2
    while True:
        fx = f_d(x)
        if abs(fx) <= eps:
            return x,k
        if f_dd(x) < 0:
            return -1,-1
        x = x - f_d(x)/f_dd(x)
        k+=1

def solve_algo_kas(a,b,eps):
    x,n = search(a,b,eps)
    if n<0:
        return 'No values'
    y = f(x)
    result = [x,y,n]
    values  = list(map(lambda x: round(float(x),len(str(eps))- 2), result))
    for val in values:
        print(f'{val} {type(val)} check type')
    return values   

