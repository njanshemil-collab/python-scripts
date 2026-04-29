marks={}
for i in range(3):
 print("enter names and mark")
 name=input("name: ")
 scor=input("mark: ")
 marks[name]=scor
print("enter the student name")
name=input("name ")
if name in marks: 
  print(marks[name])
else:
  print("enter existing name ") 