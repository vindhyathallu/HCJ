x=int(input())
for i in range(2,x):
    if x%i==0:
        flag=1
        break

if flag==1:
    print("it is not prime")
else:
    print("it is a prime")