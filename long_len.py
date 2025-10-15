words=input("enter words separated by space:").split()
largest_length=max(len(word) for word in words)
print("Length of the largest word:",largest_length)
