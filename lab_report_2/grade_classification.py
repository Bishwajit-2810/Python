student_percent=float(input())

grade=""
if student_percent >=90:
    grade+="A+"

elif student_percent >=80 and student_percent<90:
    grade+="A"
elif student_percent >=70 and student_percent<80:
    grade+="B"
elif student_percent >=60 and student_percent<70:
    grade+="C"
else :
    grade+="fail"

print(grade)