a, b = map(int, input("Enter range: ").split())
res = [x for x in range(a, b + 1) if int(x**0.5)**2 == x and all(int(d) % 2 == 0 for d in str(x))]
print(res)
