name=input("Enter the first person name:")
place=input("Enter the second person name:")
new_name=name.lower()
new_place=place.lower()
num=new_name.count("t")
num_1=new_name.count("r")
num_2=new_name.count("u")
num_3=new_name.count("e")
numm=new_place.count("t")
numm_1=new_place.count("r")
numm_2=new_place.count("u")
numm_3=new_place.count("e")
sum=num+num_1+num_2+num_3+numm+numm_1+numm_2+numm_3
new=new_name.count("l")
new_1=new_name.count("o")
new_2=new_name.count("v")
new_3=new_name.count("e")
neww=new_place.count("l")
neww_1=new_place.count("o")
neww_2=new_place.count("v")
neww_3=new_place.count("e")
summ=new+new_1+new_2+new_3+neww+neww_1+neww_2+neww_3
total=print(str(sum)+str(summ))#this is a string you have to convert it into int



#everthing is good in the above program instead of serching every name individualy initially concanate the two and then serch then the process will be simpler
#and efficient

combine_str=name+place
final=combine_str.lower()
t=final.count("t")
r=final.count("r")
u=final.count("u")
e=final.count("e")
true=t+r+u+e
l=final.count("l")
o=final.count("o")
v=final.count("v")
e_=final.count("e")
love=l+o+v+e_
score=str(true)+str(love)
fin_score=int(score)
if(fin_score<=10 and fin_score>90):
    print(f"You are coke and mentos and your true love percentage is:{fin_score}")
elif(fin_score>=40 and fin_score<=50):
    print(f"You are good to gether and your percentage is:{fin_score}")
else:
    print(f"The percentage is:{fin_score}")
