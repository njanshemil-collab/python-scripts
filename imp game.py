import random
n=random.randint(1,100)
print("enter the num")
s=int(input("enter: "))
while s!=n:
        if s>n:
            print("high")
        else:
            print("too low")
        s=int(input("enter: "))
print("you won")
