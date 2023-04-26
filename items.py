#program created by Nick
#program created to check the quantity, price and total of all commodities
itemsAvailableDict = {}
shoppingDict = {}
#Welcome User
username = input("Please enter your name:")
welcommess = f"Welcome to my Grocery Center {username}"
lenmess = len(welcommess)
print("*"* lenmess)
print(welcommess)
print("*" * lenmess)

#read data from text file
my_file = open("available_items.txt")
file_line = my_file.readline()
itemsAvailable = my_file.readlines()
#print(itemsAvailable)
my_file.close()

#fetch items from list and add to dictionary
print("*" * 10,"Items Available", "*" *10)
for item in itemsAvailable:
    item_name = item.split()[0]
    item_price = item.split()[1]
    print(f"{item_name}: {item_price}")
    itemsAvailableDict.update({item_name : float(item_price)})
print("*" * 30)
#print(itemsAvailableDict) 
 
proceedshopping = input("Do you wish to proceed(y/n):")  
while proceedshopping.lower() == "y":
    item_added = input("Add Item:")
    if item_added.title() in itemsAvailableDict:
        item_qty = int(input("Add Quantity:"))
        shoppingDict.update({item_added:{"quantity":item_qty,"subtotal" :itemsAvailableDict[item_added.title()]*item_qty}})
        print(shoppingDict)
    else:
        print("Unable to find the item.")
    proceedshopping = input("Do you wish to add items (y/n:):")
else:
    print("\n")
    print("*" * 10, "Bill Summary" , "*" * 10)
    print("Item    Quantity   Subtotal")
    total = 0
    for key in shoppingDict:
        print(f"{key}        {shoppingDict[key]['quantity']}             {shoppingDict[key]['subtotal']}") 
        total =shoppingDict[key]['subtotal'] + total
        print("*" * 10, f"Total: ksh {total}")
    print("*" * 5,"Thank You!!!!", "*" * 5)
    print("Hope to see you back soon")        
