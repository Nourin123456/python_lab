def calculate_simple_interest(p,t,senior):
    if senior:
        r=12
    else:
        r=10
    si=(p*r*t)/100
    return si
p=float(input("Enter Principal amount:"))
t=float(input("Enter time in years:"))
senior=input("Is the customer a senior citizen?(yes/no):")
si=calculate_simple_interest(p,t,senior)
print(f"\n Simple interest = {si:2f}")
