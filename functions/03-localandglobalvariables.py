# local and global variables

x=345
def display ():
    x=876
    print(globals()['x'])
    
print(x)
z = display
z ()
z ()
