ItemName = []
ItemPrice = []
def AddExpense():
    n = int(input("No of items you want to ADD:"))
    date = input("Enter DATE as (DD-MM-YYYY):")
    with open("python/Expense Tracker/expense.txt", "a") as f:
            f.write(f"\n\nDate:-{date}\nITEM NAME:-PRICE")
    for i in range(n):
        Name = input("Name of item no " + str(i+1) +" is:")
        Price = input("Price of item " + str(Name) +" is:")
        ItemName.append(Name) 
        ItemPrice.append(Price)
        with open("python/Expense Tracker/expense.txt", "a") as f:
            f.write(f"\n{str(ItemName[i]) +":-" + str(ItemPrice[i])}")

def ViewExpense():
        print("\nITEM NAME:-PRICE")
        for i in range(len(ItemName)):
            print(str(ItemName[i]) +":-" + str(ItemPrice[i])) 

def TotalExpense():
    a=0
    for i in ItemPrice:
        a=a+int(i)
    print("\nTotal of all the Expenses is:",a)
print("welcome to the expense tracker!!!")

temp = 0
while(temp == 0):
    print("\nEnter 1 to ADD the expense\nEnter 2 to view your expense\nEnter 3 to total your Expence\nEnter 4 to EXIT")
    UserInput = int(input("\nplease Make a choice to proceed:"))
    match UserInput:
        case 1:
            AddExpense()
        case 2:
            ViewExpense()
        case 3:
            TotalExpense()
        case 4:
            break
         