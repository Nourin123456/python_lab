def add_numbers(*nums):
    """This function adds any numbers of integers arguments abd returns the total sum."""
    return sum(nums)
result=add_numbers(10,20,30,40)
print("sum=",result)
print(add_numbers.__doc__)
