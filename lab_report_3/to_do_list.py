dict={}

while True:
    choice = int(input("1 for add task\n2 for mark task completed\n3 for display all task\n--> "))
    i=1
    if choice==1:
        task=input("add your task: ")
        dict[i]=[task,False]
        i+=1
    elif choice==2:
        task_no=int(input("enter task no: "))
        dict_list=dict[task_no][1]=True
        print("update done")
        print(dict)
        print()
    elif choice==3:
        print()
        print(dict)
        print()
    else:
        print("wrong choice try again")
        