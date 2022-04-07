def f(x):
    return pow(x,5) - pow(x,2)

def div_search_new(a,b,eps):
    n = 0 
    step = (a-b) / 4
    x = a
    st_n = 1
    while True:
        n+=1
        x1 = (x+ step)
        f1 = f(x)
        f2 = f(x1)  
        if f1 > f2:
            x = x1
            continue
        elif abs(step) <= eps:
            return x,n
        else:
            x = x1
            step = -1 * step/4 

def dv_search(a,b,eps):
    result = div_search_new(a, b, eps)
    return result
