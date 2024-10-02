def student_registration_system(student_list, registration_status):
    sum=0
    for i in range(len(registration_status)):
        if registration_status[i]=='Yes':
            sum+=1
    print(sum)
    print(len(student_list)-(sum))
    updated_list=[]
    for i in range(len(registration_status)):
        if registration_status[i]=="Yes":
            updated_list.append(student_list[i])
    
    return updated_list

student_list = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6']
registration_status = ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']

updated_list = student_registration_system(student_list, registration_status)
print(updated_list)
