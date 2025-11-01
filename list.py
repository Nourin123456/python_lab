numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
result = ['over' if num > 100 else num for num in numbers]
print("Original list:", numbers)
print("Modified list:", result)
