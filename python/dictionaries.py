roll_no={1:"Satwik",
        2:"Adithya",
        3:"Pawan"
}
print(roll_no)
print(roll_no[1])
print(roll_no[2])
print(roll_no[3])
roll_no[1]="Ganesh"
print(roll_no.get(2))
print(roll_no)
roll_no[1]={1.1:"Ganesh pilla",1.2:"Ganesh second"}
print(roll_no)
print(roll_no.keys())
print(roll_no.values())
print(roll_no.items())
print(len(roll_no))
roll_2=roll_no.copy()
print(roll_2)
print(roll_2.pop(3))
print(roll_2)
for j in roll_no:
    print(j)#this will give you keys
    print(roll_no[j])#this will give you values
for i in roll_no.items():
    print(i)#this will give you both combined
roll_2.clear()
print(roll_2)

phone=dict([("Adithya",9391175072),("Satwik",273),("Pawan",8919940787)])# for this method we use the concept of Tuples and in that we use commas but not colons
print(phone["Adithya"])

