import random
name=input("Please select a spot to lock the number inside without knowing to others without space:")#it returns a string and we can access each element in a string
list=[[1,1,1],[1,1,1],[1,1,1]]#this is a matrix
row_selected=int(name[0])
column_selected=int(name[1])
fin_row=list[row_selected-1]
fin_row[column_selected-1]="X"
print(list)