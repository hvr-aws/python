# calc code 
def calc(a,b):
    x = a+b
    y = a-b
    z = a*b
    u = a%b
    return(x,y,z,u)
result = calc(22,2)
print(result)
for i in result:
    print(i)