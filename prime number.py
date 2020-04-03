#prime numbers
n = int(input ('Please enter a number: '))
for x in range (2,n):
    if n%x==0:
        print('the given number is composite')
        break
 else:
     print('the given number is a prime number')
