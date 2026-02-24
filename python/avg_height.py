numbers=input("Please enter the height of the persons with comma:")
heights=numbers.split(",")
sum=0
# count=0
for i in heights:
    sum=sum+int(i)  #here take care that i is a string and not a int so change it into int
# for j in heights:
#     count=count+1
count=len(heights)
final=sum/count
print("The average height of the given heights is:",round(final))