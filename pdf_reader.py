import PyPDF2
print("give the pdf file ")
here=input("here :")
textfle=input("name of the text file in .txt form :")
pdf=open(here,'rb')
rd=PyPDF2.PdfReader(pdf)
for page in rd.pages:
   read=page.extract_text()
   open("rrc.txt","a").write(read)
