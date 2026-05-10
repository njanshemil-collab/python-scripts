import PyPDF2 as py
print("enter the pdf file to split ")
fle=input("here : ")
opfle=open(fle,"rb")
rdfle=py.PdfReader(opfle)
for i,p in enumerate(rdfle.pages,1):
 wrt=py.PdfWriter()
 wrt.add_page(p)
 s=str(i)
 wrt.write(open(s+".pdf","wb"))