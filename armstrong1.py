def check_armstrong(num):
    s=sum(int(d)**len(str(num)) for d in str(num))
    return s==num

