listinput=[]

def Add_menuitem():
    name = input("Enter snack name: ")
    Id = input("Enter snack id: ")
    price = int(input("Enter snack price: "))

    dictobj={
        "Name":name,
        "ID":Id,
        "Price":price
    }

    for i in listinput:
        if i["ID"] == Id:
            print("Id is already exists here!!")
            print("==============================================")
            return
    

    listinput.append(dictobj)
    print("Item added Successfully!!")
    print("==============================================")




def Remove_menuitem():
    Id = input("Enter snack id: ")

    for i in listinput:
        if i["ID"] == Id:
            listinput.remove(i)
            print("Item removed Successfully!!")
            print("==============================================")
            return

    
    print("Item not found here!! ")
    print("==============================================")

    return


    
def Update_menuitem():
    Id = input("Enter snack id: ")
    New_price = int(input("Enter snack new price: "))
    for i in listinput:
        if i["ID"] == Id:
            i["Price"] = New_price
            print("Item Updated Successfully!!")
            print("==============================================")
            return

    
    print("Item not found here!! ")
    print("==============================================")

    return



def Record_sale():
    print(listinput)
    print("==============================================")




while True :
    print("Welcome to Mumbai Munchies shop!")
    print("==============================================")
    print("Please choose one of the following options:")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Snack Availability")
    print("4. Record Sale")
    print("5. Exit")
    print("==============================================")



    choise = int(input("choose you input: "))

    if choise == 1:
        Add_menuitem()

    elif choise == 2:
        Remove_menuitem()
    
    elif choise == 3:
        Update_menuitem()

    elif choise == 4:
        Record_sale()

    elif choise == 5:
        print("You have quit!! ")
        print("==============================================")
        break;
    else:
        print("Invalid input please try again")
        print("==============================================")
        continue;