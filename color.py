color_list1=input("enter colors for list 1(space separated):").split()
color_list2=input("enter colors for list 2(space separated):").split()
result=[color for color in color_list1 if color not in color_list2]
print("colors in list1 not in list2:",result)

