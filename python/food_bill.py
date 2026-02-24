import random
#l=["Adithya","Harsha","Nikhil","Vineel","Satwik","Nnai"]
#a=random.choice(l)
#print(a)

#without using choice function

#text=input("Enter your 4 names with commas:")
#text_split=text.split(",")#The return type is a list
#a=text_split[random.randint(0,3)]
#print(a)

#what if the outputs are more and more then we cannot use this right

text=input("Enter your names with commas:")
text_split=text.split(",")
leng=len(text_split)
a=text_split[random.randint(0,leng-1)]
print(a)