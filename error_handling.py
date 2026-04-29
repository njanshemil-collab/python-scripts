while True:
 try:
  a=int(input("enter 1st number : "))
  break
 except ValueError:
  print("ValueERROR")
while True:
 try:
  b=int(input("enter 2nd number : "))
  break
 except ValueError:
  print("ValueERROR")
try:
 c=a/b
 print(c)
except ZeroDivisionError:
  print("zerodivisionERROR")