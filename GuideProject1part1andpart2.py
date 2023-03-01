# Part 1 And Pard 2 Total Codes

item_list =['Laptop','Headset','Second Monitor','Mousepad','USB Drive','External Drive']
print(item_list)

mandatory_item_list = item_list[0:3]

optional_item_list =  item_list[3:6]
print(mandatory_item_list)
print(optional_item_list)

limit = 5000

price_sheet = {
    'Laptop':1500,
    'Headset': 100,
    'Second Monitor':200,
    'Mousepad':50,
    'USB Drive':70,
    'External Drive':250
}

cart = []

def add_to_cart(item,quantity):
    cart.append((item,quantity))
    item_list.remove(item)

def create_inovice():
    total_amount_inc_tax = 0
    for item, quantity in cart:
        price = price_sheet[item]
        tax = 0.18 * price
        total = (tax + price) * quantity
        total_amount_inc_tax += total
        print('İtem: ',item, '\t', 'Price: ' ,price, '\t','Quantity: ',quantity,'\t','Tax: ',tax,'\t','Total: ',total,'\n')
    print("Afterr the taxes are applied the total amount is : " ,'\t',total_amount_inc_tax)    
    return total_amount_inc_tax 

def checkout():
    global limit
    total_amount = create_inovice()
    if limit ==0:
        print("You don't have any budget")
    elif total_amount > limit:
        print("The amount you have to pay is above yhe spending limit. you have to drop some items")
    else:
        limit -= total_amount
        print(f"The total amount(incl. taxes) you've paid is {total_amount}. You have {limit} dollars left")


add_to_cart("Laptop",1)
add_to_cart("Headset",8)
add_to_cart("Second Monitor",1)
add_to_cart("Mousepad",1)
add_to_cart("USB Drive",2)
add_to_cart("External Drive",4)

checkout()