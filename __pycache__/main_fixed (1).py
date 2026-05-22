# main.py
# Stationery Inventory Management System
# Python 3.0 or higher

import csv
#create a .CSV file to store the list of all the stationary items, including the item name, quantity, price, total price.
from item import StationeryItem  # Class is defined in item.py
#the class StationaryItem is from the file called item.py

# Dictionary to store all stationery items
inventory = {}


# ── Option 1: Add new item ──────────────────────────────────────────────────
def add_item():
    while True:
        name = input("Enter item name: ").strip()
        # .strip() removes any extra spaces the user accidentally types before or after the name
        # e.g. "  Pen  " becomes "Pen"

        if name == "":
            print("Item name cannot be empty. Please try again.")
            # If the user just pressed Enter without typing anything, ask again

        elif name.replace(" ", "").replace(".", "").replace("-", "").isdigit():
            print("Invalid input! Item name cannot be just numbers. Please enter a proper name (e.g. 'Pen').")
            # .replace(" ", "") removes spaces so "1 2 3" is treated as "123"
            # .replace(".", "") removes decimal points so "1.5" is treated as "15"
            # .replace("-", "") removes negative signs so "-1" is treated as "1"
            # .isdigit() then checks if what's left is purely numbers
            # This blocks entries like "123", "1.5", "999" from being used as item names
            # e.g. "123".isdigit() → True → rejected
            # e.g. "Pen".isdigit() → False → accepted

        elif any(char.isdigit() for char in name):
            print("Invalid input! Item name cannot contain numbers. Please enter a proper name (e.g. 'Pen').")
            # 'any(...)' checks if at least ONE character in the name is a digit
            # 'char.isdigit()' returns True if that single character is a number (0–9)
            # This blocks entries like "Pen123", "P3ncil", "3raser"
            # e.g. for "Pen1": 'P'.isdigit()=False, 'e'.isdigit()=False, 'n'.isdigit()=False, '1'.isdigit()=True → rejected
            # e.g. for "Pen": all characters return False → accepted

        else:
            break
            # Only reaches here if the name is non-empty and contains no digits at all
            # e.g. "Pen", "Glue Stick", "Writing Book" → all valid, exit the loop
    # Quantity input with ValueError + negative check
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a positive number.")
                continue
        # continue skips the code its suppose to run, skip it, but runs the code after the skipped code    
            break
        except ValueError:
            print("Invalid input! Quantity must be a whole number.")

# Price input with ValueError + negative check
    while True:
        try:
            price = float(input("Enter price: $"))
            if price < 0:
                print("Price cannot be negative. Please enter a positive number.")
                continue
            
            # variables to store stationary quantity and price
            new_item = StationeryItem(name, quantity, price)
            # a variable to store the class from item.py
            inventory[name] = new_item
            # dictionary variable name[variable to store stationary name]variable to store the class from item.py
            print(f"{name} added successfully with total price ${new_item.total_price:.2f}")
            #strings organised because there are also variables in them
            break
        except ValueError:
            print("Invalid input! Price must be a number (e.g. 1.20).")



# ── Option 2: Edit existing item ────────────────────────────────────────────
def edit_item():
    name = input("Enter the name of the item to edit: ")
    # Ask the user which item they want to edit
    if name in inventory:
        # Check if the item exists in the inventory dictionary

        while True:
        # Keep asking until valid inputs are given
            try:
                new_quantity = int(input("Enter new quantity: "))
            # Ask for new quantity and convert to integer

                new_price = float(input("Enter new price: $"))
            # Ask for new price and convert to float
        #same variable names, but in different functions. 
                if new_price < 0:
                    print("Price cannot be negative. Please enter a positive number.")
                    continue

                inventory[name] = StationeryItem(name, new_quantity, new_price)
            # If both inputs are valid, update the item in inventory
        # dictionary variable name[variable to store stationary name] = #the class StationaryItem is from the file called item.py
                print(f"{name} updated successfully!")
            # Confirm success to the user
        #strings organised because there are also variables in them
                break  # exit the loop after successful update

            except ValueError:
                print("Invalid input! Quantity must be a whole number and price must be a number.")
                # Catch invalid input (like letters instead of numbers)
    
    else:
        print("Error: Item not found in inventory.")
        # If the item name is not found in inventory



# ── Option 3: Update sold item ──────────────────────────────────────────────
def update_sold():
    name = input("Enter the name of the item sold: ")
    # Ask the user which item was sold
    if name in inventory:
    # Check if the item exists in the inventory dictionary
        while True:
        # Keep asking until valid input is given
            try:
                sold_qty = int(input("Enter quantity sold: "))
                # Ask for the quantity sold and convert to integer
                if sold_qty <= 0:
                # Failsafe: sold quantity must be positive
                    print("Error: Quantity sold must be positive.")
                    continue
                if sold_qty > inventory[name].quantity:
                # Failsafe: sold quantity cannot exceed available stock
                    print("Error: Not enough stock available.")
                    continue
            
                inventory[name].quantity -= sold_qty
            # Deduct sold quantity and recalculate total
                inventory[name].total_price = inventory[name].calculate_total()
                # Recalculate the total price using the item's method
                print(f"{sold_qty} {name}(s) sold. Remaining stock: {inventory[name].quantity}")
            # Confirm success to the user with updated stock info
                break
            except ValueError:
            # Catch invalid input (like letters instead of numbers)
                print("Invalid input! Quantity must be a whole number.")
    else:
        print("Error: Item not found in inventory.")
        # If the item name is not found in inventory


# ── Option 4: Display all items ─────────────────────────────────────────────
def display_items():
    if not inventory:
    # Check if the inventory dictionary is empty
    # If empty, tell the user there are no items
        print("No items in inventory.")
        return
    print("\nCurrent Inventory:")
    # If inventory has items, print a header message
    print("{:<15}{:<10}{:<10}{:<12}".format("Name", "Quantity", "Price", "Total Price"))
    # Print the table header with column names
    # {:<15} means left-align text in a space of 15 characters
    # This keeps the table neat and aligned

    print("-" * 50)
    # Print 50 dash lines, top to bottom to separate header from data

    for item in inventory.values():
    # Loop through all items stored in the inventory dictionary

        print("{:<15}{:<10}{:<10.2f}{:<12.2f}".format(
            item.name, item.quantity, item.price, item.total_price
        ))
        # Print each item's details in a formatted row
        # item.name → the name of the stationery item
        # item.quantity → how many are in stock
        # item.price → the price of one unit
        # item.total_price → total value (quantity × price)
        # .2f means show 2 decimal places for price values


# ── Option 5: Save to CSV ───────────────────────────────────────────────────
def save_to_csv(filename="inventory.csv"):
# 'filename' is the name of the file where data will be saved.
# Default is "inventory.csv", but you can change it when calling the function.
# Example: save_to_csv("backup.csv") will save to backup.csv instead.

    if not inventory:
    # Check if the inventory dictionary is empty
        print("No items to save.")
        # If empty, tell the user there are no items to save
        return # Exit the function early
    try:
        with open(filename, mode="w", newline="") as file:
        # 'open' is a built-in Python function to work with files. This means thhe program will open the file for me.
        # Parameters, which is Brackets:
        #   filename -> the file name (e.g., "inventory.csv")
        #   mode="w" -> 'w' means "write mode". It will create a new file or overwrite an existing one.
        #   newline="" -> prevents extra blank lines when writing rows on Windows systems.
            writer = csv.writer(file)
            # Create a CSV writer object using the csv module.
            # A "writer object" is a helper tool that knows how to write rows of data into a CSV file.
            # A "CSV writer object" specifically formats data into comma-separated values (CSV).

            writer.writerow(["Name", "Quantity", "Price", "Total Price"])  # Header row
            # Write the header row (column names) at the top of the CSV file
            
            for item in inventory.values():
            # Loop through all items in the inventory dictionary

                writer.writerow([item.name, item.quantity, item.price, round(item.total_price, 2)])
                # Write each item's details as a row in the CSV file
                # round(item.total_price, 2) ensures the total price is shown with 2 decimal places

        print(f"Inventory saved successfully to {filename}")
        # Confirm success to the user
        

    except IOError as e:
     # IOError is a type of error that happens when something goes wrong with file operations.
        # Examples:
        #   - File cannot be opened (maybe locked by another program)
        #   - Disk is full
        #   - No permission to write in the folder
        # 'e' contains the exact error message from Python.

        print(f"File error: {e}")



# ── Insight Functions (Bonus / Q6) ───────────────────────────────────────────
def highest_value_item():
    if not inventory:
    # Check if inventory is empty
        print("No items in inventory.")
        return
    highest = max(inventory.values(), key=lambda item: item.total_price)
    # Find the item with the highest total price
    # 'max' finds the item with the largest value based on a key
    # 'inventory.values()' gives all the StationeryItem objects stored in the dictionary
    # 'key=lambda x: x.total_price' means: for each item (x), use its total_price as the comparison value
    # lambda here is a mini function: lambda x -> return x.total_price
    print(f"Highest stock value item: {highest.name} (${highest.total_price:.2f})")

def lowest_stock_item():
    if not inventory:
    # Check if inventory is empty
        print("No items in inventory.")
        return
    lowest = min(inventory.values(), key=lambda item: item.quantity)
    # 'min' finds the item with the smallest value based on a key
    # 'key=lambda x: x.quantity' means: for each item, compare by its quantity
    # lambda here is a mini function: lambda x -> return x.quantity
    print(f"Lowest stock item: {lowest.name} (Quantity: {lowest.quantity})left — might need restocking soon.")

def total_inventory_value():
    if not inventory:
    # Check if inventory is empty
        print("No items in inventory.")
        return
    total = sum(item.total_price for item in inventory.values())
    print(f"Total inventory value: ${total:.2f}-— the overall worth of your stationery stock.")
    # 'sum' adds up all values in a sequence
    # 'item.total_price for item in inventory.values()' is a generator expression
    # It goes through each item and takes its total_price
    

def average_price():
    if not inventory:
    # Check if inventory is empty
        print("No items in inventory.")
        return
    avg = sum(item.price for item in inventory.values()) / len(inventory)
    # 'sum(item.price for item in inventory.values())' adds up all item prices
    # 'len(inventory)' counts how many items are in the dictionary
    # Dividing total price sum by len(inventory) gives the average price per item
    print(f"Average price per item: ${avg:.2f}--typical cost per item in your shop")


# ── Main Menu ────────────────────────────────────────────────────────────────
def main_menu():
    while True:
    # 'while True' creates an infinite loop so the menu keeps showing until the user exits
        print("\n====================================================")
        print("      STATIONERY INVENTORY MANAGEMENT SYSTEM")
        print("====================================================")
        print("1 - To enter new stationery item")
        print("2 - To edit the stationery item")
        print("3 - To update the stationery item which was sold")
        print("4 - To display all the stationery items")
        print("5 - To save the list of all the stationery items in .CSV file")
        print("6 - To view insights")
        # Print menu header with formatting

        choice = input("Enter option (1-6): ")
        # Ask the user to choose an option
                                                                       
        # Match the user's choice with the correct function
        if choice == "1":
            add_item()
            # Calls Option 1 function
        elif choice == "2":
            edit_item()
            # Calls Option 2 function
        elif choice == "3":
            update_sold()
            # Calls Option 3 function
        elif choice == "4":
            display_items()
            # Calls Option 4 function
        elif choice == "5":
            save_to_csv()
            # Calls Option 5 function
        elif choice == "6":
            print("\n--- Inventory Insights ---")
            highest_value_item()
            # Calls function to show most valuable item
            lowest_stock_item()
            # Calls function to show lowest stock item
            total_inventory_value()
            # Calls function to show total value of inventory
            average_price()
            # Calls function to show average price of items
        else:
        # If user enters something outside 1–6
            print("Invalid option! Please enter a number between 1 and 6.")

        # Ask user whether to continue
        while True:
            cont = input("\nDo you want to continue? (y/n): ").strip().lower()
            if cont == "y":
                print("\n" * 50)  # Scroll past old output instead of clearing
                break
                # Go back to the main menu loop
            elif cont == "n":
                print("Exiting program...")
                return
                # Go back to the main menu loop
            else:
                print("Invalid input! Please enter 'y' or 'n'.")


# ── Entry point ──────────────────────────────────────────────────────────────
main_menu()