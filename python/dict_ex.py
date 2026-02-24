student_marks={
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}
student_grade={}
for i in student_marks:
    k=0
    k=student_marks[i]
    if(k>=91 and k<=100):
        student_grade[i]="A+"
    elif(k>=81):
        student_grade[i]="A"
    elif(k>=71):
        student_grade[i]="B+"
    elif(k>=61):
        student_grade[i]="B"
    elif(k>=51):
        student_grade[i]="C"
    elif(k>=41):
        student_grade[i]="D"
    else:
        student_grade[i]="F"

print(student_grade)