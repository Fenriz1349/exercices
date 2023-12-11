N=int(input("entrez un nombre"))
x = 0
y = 1
print (x)
print (y)
for i in range(2,N) :
    n=x+y
    x=y
    y=n
    print(n)