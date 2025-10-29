n=int(input("Enter a number:"))
temp=n
sum=0
count=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**count
    n//=10
if sum==temp:
    print(temp,"is an Armstrong number")
else:
    print(temp,"is not an Armstrong number")
