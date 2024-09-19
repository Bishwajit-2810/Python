grocery_items = {} 

while True: 
    print("\nChoose an option:") 
    print("1. Add Item") 
    print("2. Remove Item") 
    print("3. View Basket") 
    print("4. Exit")   

    choice = input("Enter your choice (1/2/3/4): ")  

    if choice == '1': 
        item = input("Enter item: ")
        if item in grocery_items:
            print("already exists") 
        else: 
            grocery_items[item] = 1 
        print("item added") 
    elif choice == '2': 
        item = input("Enter the item name to remove: ")
        if item not in grocery_items:
            print("item not found")  
        else: 
            del grocery_items[item]
        print("item removed")

    elif choice == '3': 
        if len(grocery_items)==0:
            print("empty")
        else:
            print("items list:")
        for item, count in grocery_items.items():
            print(f" {item}: {count}")
    elif choice == '4': 
        print("Exiting")
        break   
    else:
        print("invalid choice")


