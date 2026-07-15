import json

expenses_list=[]                                                         # creating a list   
expense_dict={}     
user_category=0

def display_menu():                                                      # Display the menu
    print('''===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. View Total Expense
4. Search Expenses
5. Delete Expense
6. Update Expense
7. Exit''')
    
def add_expense():
    expense_dict={
    "amount":float(input("Enter the amount: ")),
    "category":input("Enter the category: ")
        }
    expenses_list.append(expense_dict)

def view_expenses():
    for i,expense in enumerate(expenses_list,start=1):
            print(f"Expense {i}")
            print(f"Amount   : ₹{expense['amount']}")
            print(f"Category : {expense['category']}")
            print("--------------------------------------")

def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses_list,file,indent=4)                               #dump ---> to save/into file


def load_expenses():
    global expenses_list
    try:
        with open("expenses.json","r") as file:
            expenses_list=json.load(file)

    except FileNotFoundError:
        expenses_list=[]

load_expenses()                                                    #load once its more like whatsapp first load all chats and then use app

while True:
    display_menu()                                                  #User enters their choice
    choice=input("Enter your choice: ")

    if choice=="1":
        add_expense()
        save_expenses()

        print("Yayy!Expense added successfully!🥳")


    elif choice=="2":
        if not expenses_list:
            print("No expenses added yet.")
        else:
            view_expenses()
        

    elif choice=="3":
        total=0
        for expense in expenses_list:
            total+=expense["amount"]
        print(f"Total expense:₹{total}")


    elif choice=="4":
        user_category=input("Enter your category: ")
        found=False
        for expense in expenses_list:
            
            if expense["category"].lower()==user_category.lower():
               found=True
               print(f"Amount   : ₹{expense['amount']}")
               print(f"Category : {expense['category']}")
               print("--------------------------------------")
        if not found:
            print("Expenses not found in this category😕")


    elif choice=="5":
        if not expenses_list:
            print("No Expenses are there to delete")
        else:
            view_expenses()

            expense_number=int(input("Enter the expense number to delete:"))
            index=expense_number-1
            if 0 <= index < len(expenses_list):
                expenses_list.pop(index)
                save_expenses()
                print("Expense deleted successfully..!!")
            else:
                print("Invalid expenses number❌")

    elif choice=="6":
        if not expenses_list:
            print("No expenses are there to update")
        else:
            view_expenses()

            expense_number=int(input("Enter the expense number to update the expenses:"))
            index=expense_number-1
            if 0<= index < len(expenses_list):
                new_amount=float(input("Enter the new amount: "))
                new_category=input("Enter the new category: ")

                expenses_list[index]["amount"]=new_amount
                expenses_list[index]["category"]=new_category

                save_expenses()

                print("Expenses are updated successfully")
            else:
                print("Invalid expense number❌")

    elif choice=="7":
        print("Goodbye!!")
        break


    else:
        print("Invalid❌")



