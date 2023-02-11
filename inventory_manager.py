#=== Create Class ===#
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Function to display product cost
    def get_cost(self):
        print(f"{self.product} Cost: {self.cost}")

    # Function to display product quantity
    def get_quantity(self):
        print(f"{self.product} Quantity: {self.quantity}")

    # Display a string representation of the Shoe class
    def __str__(self):
        return f"Country: {self.country}" \
               f"\nCode: {self.code}" \
               f"\nProduct: {self.product}" \
               f"\nCost: {self.cost}" \
               f"\nQuantity: {self.quantity}"

# Create a list to store shoe objects
shoe_list = []

#=== Define Functions ===#
# Print error when input cannot be cast to integer
def int_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Oops, you did not type a number!")

# Print error when input cannot be cast to float
def float_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Oops, you did not type a number!")

# Update inventory
def update_inventory():
    with open("inventory.txt", "w") as f:
        f.write("Country,Code,Product,Cost,Quantity")
        for shoe in shoe_list:
            f.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")

# Read shoes from inventory file and create Shoe objects
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            # Skip first line in text file
            next(f)
            # Create variables from item details
            for line in f.readlines():
                temp = line.strip().split(",")
                country = temp[0]
                code = temp[1]
                product = temp[2]
                cost = float(temp[3])
                quantity = int(temp[4])
                # Create Shoe objects with variables as instance attributes
                shoe = Shoe(country, code, product, cost, quantity)
                # Append objects to shoe list
                shoe_list.append(shoe)
    # Print error message if the file does not exist
    except FileNotFoundError:
        print("Inventory file could not be found")
        # Ask User to try again later and end program
        print("Please try again later.")
        exit()

# Append shoe object to shoe list
def capture_shoes():
    # Ask user for shoe instance attributes
    print("Enter the following information:")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = float_input("Cost: ")  # Ask user to re-enter cost if input cannot be cast to float
    quantity = int_input("Quantity: ")  # Ask user to re-enter quantity if input cannot be cast to integer

    # Create new shoe object and add to shoe list
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    # Update inventory text file
    update_inventory()
    print(f"{product} was added to inventory")

# Print shoe details
def view_all():
    for item in shoe_list:
        print(f"{item}\n")

# Find product with the lowest quantity in shoe list and update quantity
def re_stock():
    lowest_quantity_shoe = min(shoe_list, key=lambda shoe:shoe.quantity)
    print(f"Product with the Lowest Quantity:\n{lowest_quantity_shoe}")
    while True:
        # Ask user if they want to update the quantity of this product
        option = input("\nWould you like to update this product's quantity in the inventory?"
              "\n1 - Yes \n2 - No \nEnter here: ").lower()
        # Option 1 - Update quantity
        if option == "1" or option == "yes":
            # Ask user for new quantity
            new_quantity = int_input("\nEnter new quantity: ")  # Ask again if input cannot be cast to int
            # Change the object's quantity
            lowest_quantity_shoe.quantity = new_quantity
            # Update the inventory file
            update_inventory()
            print(f"{lowest_quantity_shoe} quantity was updated")
            break
        elif option == "2" or option == "no":
            break
        else:
            print("Invalid input, please try again.")

# Find shoe from inputted code and print product information
def search_shoe():
    shoe_code = input("Enter code: ").upper()
    # Check if shoe code is in shoe list
    if shoe_code in shoe_list:
        # Iterate through shoe list to search for matching code
        for shoe in shoe_list:
            if shoe.code == shoe_code:
                print(shoe)
    else:
        print("Product does not exist")

# Calculate and print the total value of each item in inventory
def value_per_item():
    # Iterate through shoe list
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} Total Value: {value:.2f}")

# Print product with the highest quantity as for sale
def highest_qty():
    # Find the product with the highest quantity
    highest_quantity_shoe = max(shoe_list, key=lambda shoe:shoe.quantity)
    # Print a message that the shoe is on sale
    print(f"SALE ITEM: \n{highest_quantity_shoe}")

#=== Main Menu ===#
# Add items from inventory to shoe list
read_shoes_data()

menu_choice = ""
# Display Main Menu
while menu_choice != 7:
    menu_choice = int_input("\n-MAIN MENU-\n"
                        "\n1. View Inventory"
                        "\n2. Add Product to Inventory"
                        "\n3. Find the Lowest Quantity Product"
                        "\n4. View Sale Product"
                        "\n5. Search Inventory by Product Code"
                        "\n6. Display Total Value of Each Product in Stock"
                        "\n7. Quit"
                        "\n\nType a number to go to the corresponding program: ")  # Ask again if input cannot be cast
    print("")                                                                      # to integer

    # View Inventory
    if menu_choice == 1:
        view_all()

    # Add Product to Inventory
    elif menu_choice == 2:
        capture_shoes()

    # Find the Lowest Quantity Product
    elif menu_choice == 3:
        re_stock()

    # View Sale Product
    elif menu_choice == 4:
        highest_qty()

    # Search Inventory by Product Code
    elif menu_choice == 5:
        search_shoe()

    # Display Total Value of Each Product in Stock
    elif menu_choice == 6:
        value_per_item()

    # Quit
    elif menu_choice == 7:
        print("Goodbye!")

    # Error Message if User Does Not Pick a Valid Option
    else:
        print("Oops, you did not choose an option! Please try again.")
