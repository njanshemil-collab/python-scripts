def txt_clean(a):
    b=a.strip()
    c=b.split()
    x=" ".join(c)
    return x
a=input("enter the messy string : ")
a=txt_clean(a)
print(a)