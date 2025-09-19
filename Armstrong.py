print("Armstrong number check")
num=input("enter a number:")
length=len(num)
total=0
for digit in num:
	total+=int(digit)**length
if total==int(num):
	print("yes, its Armstrong")
else: 
	print("No,its not armstrong")
