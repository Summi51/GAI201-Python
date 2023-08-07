dishitem=[{"ID":1,"Name":"samosa","Quantity":10,"Price":20},{"ID":2,"Name":"momo","Quantity":5,"Price":10},
      {"ID":3,"Name":"pizza","Quantity":8,"Price":100}]

orderItem=[]
def Add_dishitem():
    name=(input("Enter Dish Name: "))
    Id=int(input("Enter Dish ID: "))
    price=int(input("Enter Dish Price: "))
    quantity=int(input("Enter Dish Quantity: "))


    dicItem={
        "ID":Id,
        "Name":name,
        "Price":price,
        "Quantity":quantity
    }


    for i in range(len(dishitem)):
        if dishitem[i]["ID"]==Id:
            print()
            print("Dish already exist with this Id")
            print("==============================================")
            print()
            return 


    dishitem.append(dicItem)
    print()
    print("Dish Added Successfully !!")
    print("==============================================")


def Show_Menu():
    print()
    print(dishitem)
    print()

def Remove_dishitem():
    print("\n")
    Id=int(input("Enter Dish ID: "))

    for i in range(len(dishitem)):
        if dishitem[i]["ID"]==Id:
            dishitem.pop(i)
            print()
            print("Dish Removed Successfully !!")
            print("==============================================")
            print()
            return 
    print()    
    print("Item doesn't exist")  
    print("==============================================")
    print()   

def Update_Availablity():
    Id=int(input("Enter Dish ID: "))
    Inc=int(input("Enter Quantity You want to increase: "))

    for i in range(len(dishitem)):
        if dishitem[i]["ID"]==Id:
            dishitem[i]["Quantity"]=dishitem[i]["Quantity"]+Inc
    print()
    print("Quantity Increased Successfully")
    print("==============================================")
    print()


def New_Order():
    Name=(input("Enter your Name: "))
    Id=int(input("Enter Dish ID: "))
    quantity=int(input("Enter Quantity : "))
  
    dicItem={
         "Name":Name,
         "ID":Id,
         "status":"pending"
     }
    for i in range(len(dishitem)):
         if dishitem[i]["ID"]==Id:
             if dishitem[i]["Quantity"]>0:
              dicItem["dishitem"]=dishitem[i]["Name"]
              dicItem["price"]=dishitem[i]["Price"]*quantity
              dishitem[i]["Quantity"]=dishitem[i]["Quantity"]-quantity
        
             else:
                 print()
                 print("Item is not available in stock" )
                 print("==============================================")
                 print()

    orderItem.append(dicItem) 
    print()  
    print("order has done successfully")    
    print("==============================================")
    print() 




def Update_order_status():
     Id=int(input("Enter Dish ID: "))
     
     for i in range(len(orderItem)):
         if orderItem[i]["ID"]==Id:
             orderItem[i]["status"]="recieved"
             print()
             print("order status changed successfully")
             print("==============================================")
             print()
             return 
     print()   
     print("Order with this Id does not exist here")
     print("==============================================")
     print()

def Review_Order_status():
    print(orderItem)

while True:
    print("Welcome to Zesty Zomato")
    print("==============================================")
    print("Choose 1 option out of this")
    print("1. Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Update Availablity") 
    print("5. New Order") 
    print("6. Update order Status")
    print("7, Review all orders")
    print("8. Exit")

    choice = int(input("choose you input: "))

    if choice==1:
        Show_Menu()

    elif choice==2:
        print("\n")
        Add_dishitem()

    elif choice==3:
        Remove_dishitem()

    elif choice==4:
        Update_Availablity()

    elif choice==5:
        New_Order()  

    elif choice==6:
        Update_order_status()

    elif choice==7:
        Review_Order_status()

    elif choice==8:
        print("You have quit here!! ")
        break;
    else:
        print("Invalid Input please try again !!")
        continue