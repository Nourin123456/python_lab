number=list(map(int,input("enter integers separated by spaces:").split()))
result=["over" if n>100 else n for n in number]
print("processed list:",result)
