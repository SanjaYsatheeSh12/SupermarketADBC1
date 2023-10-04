print("\t\t\t\tABC Supermarket")
list1=["Groceries","Meat","shampoos","Bakery","Non food goods"]
while True:
    print("To Add Items to the list,enter A")
    print("to remove items from the list,enter B")
    print("To display the Items in list,enter C")
    print("To exit from the menu,enter D")
    choice=input("Enter the number corresponding to the option:")
    if choice=="A":
        newitem=str(input("Enter the item You want to add to the list:"))
        list1.append(newitem)
        print("\nList after updation is:\n",list1,"\n\n\n\n")
    elif choice=="B":
        print(list1)
        delete1=str(input("Enter the item you want to remove from the list:"))
        if delete1 in list1:
            list1.remove(delete1)
            print("\n",list1,"\n\n\n\n")
        else:
            print("\nThe item you entered is not in the list!!\n\n\n\n")
    elif choice=="C":
        print("\n",list1)
    elif choice=="D":
        print("\nexiting program.....")
        break
    else:
        print("\nwrong input,exiting program")
        break