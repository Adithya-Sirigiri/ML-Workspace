def add_new_student(name,roll,age,course):
    student_data.append({"Name":name,"roll_no":roll,"age":age,"course":course})
student_data = [
    {
        "Name": "Ram",
        "roll_no": 10,
        "age": 20,
        "course": "Python"
    },
    {
        "Name": "Mohan",
        "roll_no": 20,
        "age": 22,
        "course": "Java"
    }
]
add_new_student("Shyam",22,18,"C++")
print(student_data)
