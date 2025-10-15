text=input("Enter a sting:")
for char in set(text):
	print(f"'{char}':{text.count(char)}")
