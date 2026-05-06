def sum(a,b):
    return a+b
print(sum(5,2))

def n_sum(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total
print(n_sum(10))

def eve_odd(n):
    if n%2==0:
        return "Even"
    if n%2!=0:
        return "Odd"
eve_odd(4)