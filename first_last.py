colors=input("Enter color names separated by commas:")
color_list=colors.split(",")
color_list=[color.strip() for color in color_list]
print("Color List:",color_list)
print("first color:",color_list[0])
print("last colot:",color_list[-1])
