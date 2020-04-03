#this program show how the covid 19 spreads taking an example if one person can spread to 2 people 
x=0
people=2
for i in range(0,6):
    y=people**i
    x+=y
print('total= ',x)

