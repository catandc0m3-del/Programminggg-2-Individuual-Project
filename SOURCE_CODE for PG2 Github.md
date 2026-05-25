# 🗂️ Source Code Documentation
## Stationery Inventory Management System

This document explains how the source code works — what each file does, what each function does, and how they connect together.

---

## 📁 Project Structure

```
project/
│
├── main.py          # Main program — contains all menu functions and program logic
└── stationery.py    # Contains the StationeryItem class
```

---

## 📄 File 1: `stationery.py`

This file defines the **blueprint** (class) for a stationery item.

```python
class StationeryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = self.calculate_total()

    def calculate_total(self):
        return self.quantity * self.price
```

### Class: `StationeryItem`

| Part | Description |
|---|---|
| `__init__` | Constructor — runs automatically when a new item is created. Sets `name`, `quantity`, `price`, and calculates `total_price`. |
| `self.name` | Stores the item's name (e.g. `"Pen"`) |
| `self.quantity` | Stores how many units are in stock |
| `self.price` | Stores the price of one unit |
| `self.total_price` | Stores the result of `quantity × price`, calculated automatically |
| `calculate_total()` | Multiplies `quantity` by `price` and returns the result |

**Example of how it works:**
```python
item = StationeryItem("Pen", 50, 1.50)
# item.name        → "Pen"
# item.quantity    → 50
# item.price       → 1.50
# item.total_price → 75.0
```

---

## 📄 File 2: `main.py`

This is the main program file. It imports `StationeryItem` from `stationery.py` and uses a dictionary called `inventory` to store all items.

```python
import csv
from stationery import StationeryItem

inventory = {}  # Dictionary to store all stationery items
```

The `inventory` dictionary stores items like this:

```python
inventory = {
    "Pen": <StationeryItem object>,
    "Ruler": <StationeryItem object>
}
```

---

### 🔧 Function 1: `add_item()`

**Purpose:** Adds a brand-new item to the inventory.

```python
def add_item():
```

**Step-by-step logic:**

1. **Name validation loop** — keeps asking until a valid name is entered:
   - Rejects empty input
   - Rejects names made up entirely of numbers (e.g. `"123"`)
   - Rejects names that contain any digit (e.g. `"Pen1"`)

2. **Quantity input loop** — uses `try/except` to catch non-integer input:
   - Rejects negative numbers
   - Only accepts whole numbers (`int`)

3. **Price input loop** — uses `try/except` to catch non-number input:
   - Rejects negative numbers
   - Accepts decimals (`float`)

4. **Creates** a `StationeryItem` object and stores it in `inventory[name]`.

**Key concepts used:**
| Concept | Where |
|---|---|
| `.strip()` | Removes extra spaces from item name input |
| `.isdigit()` | Checks if a string contains only numbers |
| `any(char.isdigit() for char in name)` | Checks if any character in the name is a digit |
| `try / except ValueError` | Catches invalid number input |
| `continue` | Skips back to the top of the loop |
| `break` | Exits the loop when input is valid |

---

### 🔧 Function 2: `edit_item()`

**Purpose:** Updates the quantity and price of an existing item.

```python
def edit_item():
```

**Step-by-step logic:**

1. Asks for the name of the item to edit.
2. Checks if the name exists in `inventory` using `if name in inventory`.
3. If found: asks for new quantity and price, then replaces the old item with a new `StationeryItem` object.
4. If not found: prints an error message.

**Key concepts used:**
| Concept | Where |
|---|---|
| `if name in inventory` | Checks if the key exists in the dictionary |
| `try / except ValueError` | Catches invalid number input |
| `inventory[name] = StationeryItem(...)` | Replaces the existing item with an updated one |

---

### 🔧 Function 3: `update_sold()`

**Purpose:** Reduces stock when an item is sold.

```python
def update_sold():
```

**Step-by-step logic:**

1. Asks which item was sold.
2. Checks if the item exists in `inventory`.
3. Asks how many were sold — validates that:
   - The quantity is positive (`> 0`)
   - The quantity does not exceed current stock
4. Deducts the sold quantity from `inventory[name].quantity`.
5. Recalculates `total_price` by calling `calculate_total()`.

**Key concepts used:**
| Concept | Where |
|---|---|
| `inventory[name].quantity -= sold_qty` | Deducts quantity directly from the object's attribute |
| `inventory[name].calculate_total()` | Calls the method from `StationeryItem` to recalculate total |
| `if sold_qty > inventory[name].quantity` | Prevents selling more than what's in stock |

---

### 🔧 Function 4: `display_items()`

**Purpose:** Prints all inventory items in a formatted table.

```python
def display_items():
```

**Step-by-step logic:**

1. Checks if `inventory` is empty — if so, prints a message and exits.
2. Prints a table header using `.format()` with fixed column widths.
3. Loops through `inventory.values()` and prints each item's details.

**Key concepts used:**
| Concept | Where |
|---|---|
| `if not inventory` | Checks if the dictionary is empty |
| `"{:<15}".format(...)` | Left-aligns text in a fixed-width column |
| `{:<10.2f}` | Shows a number with 2 decimal places in a fixed-width column |
| `for item in inventory.values()` | Loops through all `StationeryItem` objects |

**Example output:**
```
Current Inventory:
Name           Quantity  Price     Total Price
--------------------------------------------------
Pen            40        1.50      60.00
Ruler          20        0.80      16.00
```

---

### 🔧 Function 5: `save_to_csv()`

**Purpose:** Saves inventory data to a `.csv` file.

```python
def save_to_csv(filename="inventory.csv"):
```

**Step-by-step logic:**

1. Checks if `inventory` is empty — exits early if so.
2. Opens (or creates) `inventory.csv` using `open()` in write mode (`"w"`).
3. Creates a `csv.writer` object.
4. Writes the header row: `["Name", "Quantity", "Price", "Total Price"]`
5. Loops through all items and writes each as a row.
6. Uses `try / except IOError` to handle file errors (e.g. disk full, permission denied).

**Key concepts used:**
| Concept | Where |
|---|---|
| `open(filename, mode="w", newline="")` | Opens the file for writing; `newline=""` prevents blank lines on Windows |
| `csv.writer(file)` | Creates a writer object from the `csv` module |
| `writer.writerow([...])` | Writes one row of data |
| `round(item.total_price, 2)` | Rounds total price to 2 decimal places |
| `except IOError` | Catches file-related errors |

---

### 🔧 Insight Functions (Option 6)

These four functions analyse the inventory and display useful statistics.

#### `highest_value_item()`
Finds the item with the **highest total price** using `max()`.
```python
highest = max(inventory.values(), key=lambda item: item.total_price)
```

#### `lowest_stock_item()`
Finds the item with the **lowest quantity** using `min()`.
```python
lowest = min(inventory.values(), key=lambda item: item.quantity)
```

#### `total_inventory_value()`
Adds up the `total_price` of all items using `sum()`.
```python
total = sum(item.total_price for item in inventory.values())
```

#### `average_price()`
Calculates the average unit price of all items.
```python
avg = sum(item.price for item in inventory.values()) / len(inventory)
```

**Key concepts used:**
| Concept | Where |
|---|---|
| `max(..., key=lambda item: item.total_price)` | Finds the item with the highest value |
| `min(..., key=lambda item: item.quantity)` | Finds the item with the lowest value |
| `lambda` | A one-line anonymous function used as a sorting/comparison key |
| `sum(... for item in ...)` | Generator expression that sums a value across all items |
| `len(inventory)` | Returns the number of items in the dictionary |

---

### 🔧 Function: `main_menu()`

**Purpose:** The main loop that keeps the program running and routes user input to the correct function.

```python
def main_menu():
    while True:
        # Display menu...
        choice = input("Enter option (1-6): ")
        if choice == "1": add_item()
        elif choice == "2": edit_item()
        # ... and so on
```

**Step-by-step logic:**

1. `while True` runs the menu indefinitely until the user chooses to exit.
2. Prints the menu options.
3. Reads the user's choice.
4. Uses `if/elif` to call the correct function.
5. After each action, asks `"Do you want to continue? (y/n)"`:
   - `y` → clears old output and shows the menu again
   - `n` → exits the program using `return`
   - anything else → asks again

---

## 🔗 How the Files Connect

```
main.py
│
├── imports StationeryItem from stationery.py
│
├── add_item()      → creates StationeryItem objects → stores in inventory{}
├── edit_item()     → replaces StationeryItem objects in inventory{}
├── update_sold()   → modifies .quantity and calls .calculate_total()
├── display_items() → reads from inventory{}
├── save_to_csv()   → reads from inventory{} → writes to inventory.csv
└── insights        → reads from inventory{} using max(), min(), sum()
```

---

## 📊 Data Flow Summary

```
User Input
    ↓
Input Validation (loops + try/except)
    ↓
StationeryItem object created (stationery.py)
    ↓
Stored in inventory{} dictionary (main.py)
    ↓
Read / Modified / Displayed / Saved as needed
```

---

*Source code written in Python 3 · GitHub: [catandc0m3-del/Programminggg-2-Individuual-Project](https://github.com/catandc0m3-del/Programminggg-2-Individuual-Project)*
