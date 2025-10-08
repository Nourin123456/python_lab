a=list(map(int,input("Enter the first list:").split()))
b=list(map(int,input("Enter the second list:").split()))
if len(a)== len(b):
	print("same length")
else:
	print("Different length")
if sum(a)==sum(b):
	print("same sum")
else:
	print("Different sum")
common=set(a)&set(b)
if common:
	print("common values",common)
else:
	print("No common values")
