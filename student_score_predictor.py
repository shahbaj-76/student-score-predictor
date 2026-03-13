def student_details():
    name=input("Enter name of student: ")
    hours_studied=int(input("Enter hours studied: "))
    previous_percentage=int(input("Enter previous percentage : "))
    result=hours_studied*10+previous_percentage*0.2
    student={"name" : name,
             "hours_studied" : hours_studied,
             "previous_percentage": previous_percentage,
              "result": result}
    return student
students=[]
while True:
    entry=input("Do you want to enter student details? (yes/no) ").lower().strip()
    if entry=="yes" or entry=="y":
            student=student_details()
            students.append(student)
    else:
        break
print(students) 

count=0
total=0
for st in students:
     count+=1
     total+=st["result"]
     print(st["name"], "--", st["result"])
if count>0:
     avg=total/count
     print("Total score", total)
     print("Average marks", avg)
if students:
    maximum=max(students, key=lambda s:s["result"])
    minimum=min(students, key=lambda s:s["result"])
    print(f"Highest number {maximum['name']} ({maximum['result']})")
    print(f"Lowest number {minimum['name']} ({minimum['result']})")
else:
    print("No data")

