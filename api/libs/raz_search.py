
def find_min(x):
    value = pow(x,5) - pow(x,2)
    return value

def algo1(x0,x1,a,b,e, step,n):
    f0 = find_min(x0)
    f1 = find_min(x1)
    if f0 > f1:
        x0= x1 
        f0 = f1
        if  x0 > a and x0 < b:
            return algo1(x0,x1,a,b,e,step,n+1)
        else:
            if abs(step) < e:
                return x0,f0,n
            else:
                step = -1 * (step/4)
                return algo1(x0,x0 + step,a,b,e,step,n+1)
    else:
        if abs(step) < e:
            return x0,f0,n
        else:
            step = -1 * (step/4)
            return algo1(x0,x0 + step,a,b,e,step,n+1)
            
def algo(a,b,e):
    step = (b-a) / 4
    n = 0
    return algo1(a,a+step, a, b, e, step,n)

def raz_search_method(a,b,e):
    result = list(algo(a,b,e))
    values  = list(map(lambda x: round(x,len(str(e))- 2), result))
    return values
    



