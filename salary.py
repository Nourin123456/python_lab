basic_pay =float(input("Enter the basic salary of an employee:"))
hra=0.10*basic_pay
ta=0.05*basic_pay
total_salary=basic_pay+ta+hra
print("Basic pay:",basic_pay)
print("HRA (10%):",hra)
print("TA (5%):",ta)
print("total salary:",total_salary)
