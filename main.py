def greet_user(name):
    """
    Greets the user by their name.
    """
    return f"Hello, {name}! Welcome to Restaurant Manger"

def calculate_bill(items):
    """
    Calculates the total bill from a list of menu items.
    Each item is a dictionary with 'name' and 'price'.
    """
    total = 0
    for item in items:
        total += item.get('price',0)
    return total

def show_contact_info():
    """
    Displays restaurant contact information.
    """
    phone = "+91 9876543210"
    email = "contact@restaurant.com"
    print("Contact Us")
    print(f"Phone : {phone}")
    print(f"Email : {email}")

def main():
    """
    main function to demonstrate functionality.
    """
    # greet
    user_name = "Alice"
    print(greet_user(user_name))

    # calculate bill
    order_items = [
        {'name':'Pizza', 'price':200},
        {'name':'Cold drink', 'price':50},
        {'name':'Brownie', 'price': 80}
    ]
    total = calculate_bill(order_items)
    print(f"Total Bill : {total}")

    # contact info
    show_contact_info()
    
# run the script
if __name__ == '__main__':
    main()

