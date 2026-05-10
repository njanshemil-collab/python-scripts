import PyPDF2 as py
while True:
    print("Type which tool want to use among :-   read , merge , split. OR stop")
    tool=input("Tool =  ")
    if tool=="read":
        print("give the pdf file ")
        here=input("here :")
        textfle=input("name of text file in .txt form :")
        pdf=open(here,'rb')
        rd=py.PdfReader(pdf)
        for page in rd.pages:
           read=page.extract_text()
           open(textfle,"a").write(read)
        print("DONE")
    elif tool=="merge":
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
        print("DONE")
    elif tool=="split":
        print("enter the pdf file to split ")
        fle=input("here : ")
        opfle=open(fle,"rb")
        rdfle=py.PdfReader(opfle)
        for i,p in enumerate(rdfle.pages,1):
         wrt=py.PdfWriter()
         wrt.add_page(p)
         s=str(i)
         wrt.write(open(s+".pdf","wb"))
        print("DONE")
    elif tool=="stop":
       break    
    else:
       print("pls enter valid tool ")