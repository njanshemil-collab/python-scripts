def add(a,b):
  return a+b 
def sub(a,b):
  return a-b
def mult(a,b):
  return a*b
def divd(a,b):
   if b==0:
    return("ERROR due to zero division")
   else: 
    return a/b 
num1=int(input("enter the first num : "))
num2=int(input("enter the second num : "))
op=input("enter operator : ")
if op == "+":
  result= add(num1,num2)
  print("answer = ",result)
elif op == "-":
  result= sub(num1,num2)
  print("answer = ",result)
elif op == "*":
  result= mult(num1,num2)
  print("answer = ",result)
elif op == "/":

   result= divd(num1,num2)
   print("answer = ",result)
else:
  print("invalid operator")