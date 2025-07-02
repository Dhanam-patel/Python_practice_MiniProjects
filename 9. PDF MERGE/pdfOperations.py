import pypdf
import random
print("\nEnter 1 to Merge the PDF's\nEnter 2 to Get Specific portion between 2 pages of the PDF\nEnter 3 to Encrypt the PDF")
UserWish = int(input("\nPlease make a choice: "))
ranNo = random.randint(100, 1000)
match UserWish:
    case 1:
        writer = pypdf.PdfWriter()
        Userinputmg = int(input("Please Enter how many pdf do you want to merge:"))
        for i in range(Userinputmg):
            Path = input(f"Please enter the path of the pdf {i+1}:")
            reader = pypdf.PdfReader(Path)
            for pages in reader.pages:
                writer.add_page(pages)
        Storepathmg = input("Please enter the PATH to store the new PDF: ")
        with open(f"{Storepathmg}/new_{ranNo}.pdf", "wb") as output:
            writer.write(output)
    case 2:
        print("\nEnter the starting and ending page of the portion:")
        userinputpg = input("Enter the path: ")
        A = int(input("\npage 1: "))
        B = int(input("page 2: "))
        read = pypdf.PdfReader(userinputpg)
        merge = pypdf.PdfWriter()
        for i in range(A,B,1):
                merge.add_page(read.pages[i])
        Storepathpg = input("\nPlease enter the PATH to store the new PDF: ")
        with open(f"{Storepathpg}/newcreated_{ranNo}.pdf", "wb") as output:
            merge.write(output)
    case 3:
        userinputen = input("\nEnter the path: ")
        reader = pypdf.PdfReader(userinputen)
        writer = pypdf.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        password = input("\nPlease Enter the password you want to SET: ") 
        writer.encrypt(password)
        Storepathen = input("\nPlease enter the PATH to store the new PDF: ")
        with open(f"{Storepathen}/encrypted_{ranNo}.pdf", "wb") as output:
            writer.write(output)
