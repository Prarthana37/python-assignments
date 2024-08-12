#menu of the restaurant
menu={
    "sandwich":50,
     "Pizza":110,
     "Burger":100,
     "Salad":80,
     "Soup":60,
     "Tea":20,
     "Coffee":25
}
#Greetcustomer
print("Welcome to La'cafe")
print("sandwich: Rs50\nPizza: Rs110\nBurger: Rs100\nSalad: Rs80\nSoup: Rs60\nCoffee: Rs25\n")
order_Total=0 #add on of items

item_1=input("Enter the item you want=")
if item_1 in menu:
    order_Total += menu[item_1] #0+110
    print("your item_1 has been noted")
else:
    print(f"ordered item_1 is not available")

another_item=input("Would you like to have somethig else (yes/no)")
if another_item == "yes":
    item_2=input("enter the item you need=")
    if item_2 in menu:
        order_Total += menu[item_2]
        print("The item_2 is added")
    else:
        print(f"ordered item_2 is not available")
else:
    print("Total bill:",order_Total)        
 
another_item=input("Would you like to have somethig else (yes/no)")
if another_item == "yes":
    item_3=input("enter the item you need=")

    if item_3 in menu:
        order_Total += menu[item_3]
        print("The item is added")
    else:
        print(f"The item is not available")
else:
    print("Total bill:",order_Total)        
         

another_item=input("Would you like to have somethig else (yes/no)")
if another_item == "yes":
    item_4= input("enter the item you need")

    if item_4 in menu:
        order_Total += menu[item_4]
        print("The is item is added")
    else:
        print(f"The item is not available")
else:
    print("Total bill:",order_Total)       
    
print(f"The total bill amount is {order_Total}")

