import PyPDF2 as py
print("enter the 2 pdf files to merge ")
a=input("1st one : ")
b=input("2nd one : ")
newnme=input("new file name in .pdf form :")
aa=open(a,"rb")
bb=open(b,"rb")
rd1=py.PdfReader(aa)
rd2=py.PdfReader(bb)
wrt=py.PdfWriter()
for rr in rd1.pages:
    wrt.add_page(rr)
for ss in rd2.pages:
    wrt.add_page(ss)
wrt.write(open(newnme,"wb"))