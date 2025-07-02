class Books:
    ListofBooks = []
    def __init__(self, Nm, Pr,no):
        self.Name = Nm
        self.Price = Pr
        self.NOBOOKS = no
        self.ListofBooks.append(f"{self.Name} :- {self.Price}")
        with open("python/Library Management system/temp.txt", "a") as f:
                f.write(f"\n{self.Name} :- Rs.{self.Price}")
        with open("python/Library Management system/temp.txt", "r") as f:
            a = f.readlines()
        with open("python/Library Management system/temp.txt", "w") as f:
            a[0] = int(a[0])+self.NOBOOKS
            a[0] = f"{a[0]}\n"
            f.writelines(a)
print("\nWelcome to the Library Management System!!!")
print("\nEnter 1 to Add a book to the system\nEnter 2 to Find a Book from a system\nEnter 3 to EXIT")
UserInput = int(input("\nPlease make a choice:"))
match UserInput:
    case 1:
        NoOfBooks = int(input("\nplease Enter how many no of books you want to add:-"))
        for i in range(NoOfBooks):
            Bookn = input("\nPlease Enter Book name:-")
            BookP = int(input("Please Enter Book price:-"))
            a = Books(Bookn,BookP,1)
    case 2:
        UserWish = input("Please Enter the Book Name:- ")
        with open("python/Library Management system/temp.txt", "r") as f:
            a = f.readlines()
        for i in a[1:]:
            Bookname = i.split(":-")[0].strip()
            if(Bookname == UserWish):
                temp = 1
                break
            else:
                temp = 0
        if( temp == 1 ):
            print(f"Congratulations we have the book {UserWish} you were searching for")
        else:
            print(f"Sorry but we do not have the book {UserWish} you were searching for")
    case 3:
        exit