# continue is used to run if condition and skips that values
x=0
while x<20:
    x += 1
    if x%2==0:
        continue
    print(x)