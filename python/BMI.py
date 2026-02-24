w=input("Please enter the weight of the person")
h=input("Please enter the height of the person")
#BMI=int(w)/float((h**2))
BMI=int(w)/(float(h)**2)
print(BMI)

#here the problem which occured is w and h aer strings and we are dividing them so it gave type error and most importantly we are applying float for outside
#bracket and not for h so it is giving error