student_data={
    "Adithya":{"Roll_no":12413017,"Branch":"DSA","ph_no":939115072},
    "Satwik":{"Roll_no":12411107,"Branch":"CSE","ph_no":273}
}
print(student_data)
print(student_data["Adithya"])
print(student_data["Adithya"]["Roll_no"])
student_data["Adithya"]["ph_no"]=8919940787
print(student_data)
student_data["Pawan"]={"Roll_no":"JEE1067","Branch":"ME","ph_no":8978081601}
print(student_data)

#adding list to a dictionary

travel={
    "Delhi":["jantar mantar","red fort","parliment"],
    "Gujarat":["Forest"]
}
print(travel)
print(travel["Delhi"])

#adding dictionaries to list

phone_no=[
    {"Name":"Adithya","Phone":9391175072,"place":"Andhra Pradesh"},
    {"Name":"Pawan","Phone":8919940787,"place":"Visakhapatnam"}
]
print(phone_no)
print(phone_no[1])
print(phone_no[1]["Name"])