def add(a,b):
    return a+b

x=10
y=30
z=add(x,y)
print("call in assignment",z)
p=100+add(x,x)
print("call in expression",p)
print("call in output",add(y,y))

