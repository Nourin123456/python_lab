def check(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"
n=int(input("Enter a number:"))
result=check(n)
print("The number is",result)

