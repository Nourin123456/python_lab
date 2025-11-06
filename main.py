import armstrong1
low=int(input("Enter start:"))
high=int(input("Enter end:"))

for i in range(low,high + 1):
    if armstrong1.check_armstrong(i):
        print(i)
