print("enter first number")
while True:
 try:
   num1=int(input("enter: "))
   break
 except:
   print("number adikkada ") 
print("enter second number")
while True:
  try:
   num2=int(input("enter . : "))
   break
  except:
   print("number adikkada ") 
print("enter operator sign")
op=input("enter: ")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)    
elif op=="*":
    print(num1*num2)    
elif op=="/":
    if num2==0:
       print("zero division ERROR")
    else:
     print(num1/num2)
else:
    print("give valid operator ") 