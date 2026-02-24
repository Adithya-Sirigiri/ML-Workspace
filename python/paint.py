import math
len=int(input("Enter the length of the wall:"))
bre=int(input("Enter the breadth of the wall:"))
area=len*bre
coverage=7
cans=math.ceil(area/coverage)
print(cans)