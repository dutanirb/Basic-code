nested_dict = {'Soap': {'Lux': 40, 'Dove': 50, 'Lifbouy': 45, 'Dettol': 30},
               'Oil': {'Nihar': 60, 'Jasmine': 40, 'Parachute': 70, 'Bajaj': 50},
               'Shampoo': {'Sunslik': 180, 'Clinic plus': 120, 'Pantene': 150, 'Dove': 250}}
my_cart = []
my_quantity = []
my_total = []
ask_name = input("Hi! Welcome to Mystore,Please enter your name: ")
cap_name = ask_name.capitalize()
while True:
    print("Hi {}, Mystore can help you with the following items: ".format(cap_name))
    for item in nested_dict:
        print(item)
    ask_user_category = input("Please select the category: ").capitalize()
    if ask_user_category in nested_dict:
        print("Hi we have the following brand with price for {}: ".format(ask_user_category))
        for brand, price in nested_dict[ask_user_category].items():
            print(brand, ":", "₹{}".format(price))
        ask_brand = input("please select a brand you want: ").capitalize()
        if ask_brand in nested_dict[ask_user_category]:
            try:
                ask_quantity = float(input("Enter your quantity for {}: ".format(ask_brand)))
                add_quantity = nested_dict[ask_user_category][ask_brand] * ask_quantity
                print(
                    "The price of the item you have selected is {} for %d quantity".format(add_quantity) % ask_quantity)
                my_cart.append(ask_brand)
                my_quantity.append(ask_quantity)
                my_total.append(add_quantity)
                print("You have the following item added in your cart:")
                for items, quantity,prices in list(zip(my_cart,my_quantity,my_total)):
                    print("Items: {} Quantity: {} Price: ₹{}".format(items, quantity, prices))
                    total_amount = sum(my_total)
                    print("Estimated Total amount is {}".format(total_amount))
            except:
                print("Please enter a valid quantity.")
            cont_shopping = input("write Yes to continue or write anything to exit(): ").lower()
            if cont_shopping == "yes":
                continue
            else:
                print("Final cart:")
                for items, quantity,prices in list(zip(my_cart,my_quantity,my_total)):
                    print("Items: {} Quantity: {} Price: ₹{}".format(items, quantity, prices))
                total_amount = sum(my_total)
                print("Grand Total= ₹{}".format(total_amount))
                print("Thank you for shopping with Mystore.")
                break
        else:
            print("This Item is not there in Mystore.")
    else:
        print("Sorry we donot have this product.")
