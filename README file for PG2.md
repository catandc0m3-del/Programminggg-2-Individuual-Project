# 📦 Stationery Inventory Management System

A simple command-line program written in Python that helps you manage a stationery shop's inventory. You can add items, edit them, track sales, view your stock, save data to a CSV file, and view useful insights.

---

# 📋 Table of Contents

- [Requirements](#requirements)
- [Files Included](#files-included)
- [How to Run](#how-to-run)
- [Main Menu Options](#main-menu-options)
  - [Option 1 – Add New Item](#option-1--add-new-item)
  - [Option 2 – Edit Existing Item](#option-2--edit-existing-item)
  - [Option 3 – Update Sold Item](#option-3--update-sold-item)
  - [Option 4 – Display All Items](#option-4--display-all-items)
  - [Option 5 – Save to CSV](#option-5--save-to-csv)
  - [Option 6 – View Insights](#option-6--view-insights)
- [Input Rules](#input-rules)
- [Example Walkthrough](#example-walkthrough)

---

## ✅ Requirements

- **Python 3.0 or higher**
- No extra libraries needed — only the built-in `csv` module is used.

To check your Python version, open a terminal and run:

```
python --version
```

---

## 📁 Files Included

| File | Description |
|---|---|
| `main.py` | The main program — run this file to start |
| `stationery.py` | Contains the `StationeryItem` class used to calculate total price |

> ⚠️ **Both files must be in the same folder.** The program will not work if they are separated.

---

## ▶️ How to Run

1. Download or clone the project files into a folder on your computer.
2. Open a terminal (Command Prompt, PowerShell, or any terminal).
3. Navigate to the folder where the files are saved. For example:

```
cd C:\Users\YourName\Downloads\stationery-project
```

4. Run the program with this command:

```
python main.py
```

The main menu will appear on screen.

---

## 📌 Main Menu Options

When the program starts, you will see this menu:

```
====================================================
      STATIONERY INVENTORY MANAGEMENT SYSTEM
====================================================
1 - To enter new stationery item
2 - To edit the stationery item
3 - To update the stationery item which was sold
4 - To display all the stationery items
5 - To save the list of all the stationery items in .CSV file
6 - To view insights

Enter option (1-6):
```

Type a number from **1 to 6** and press **Enter**.

---

### Option 1 – Add New Item

Adds a brand-new stationery item to the inventory.

**You will be asked for:**
- **Item name** – letters only (e.g. `Pen`, `Glue Stick`)
- **Quantity** – a whole number (e.g. `50`)
- **Price** – a decimal number (e.g. `1.50`)

The total price is automatically calculated as `quantity × price`.

**Example:**
```
Enter item name: Pen
Enter quantity: 50
Enter price: $1.50
Pen added successfully with total price $75.00
```

---

### Option 2 – Edit Existing Item

Updates the quantity and price of an item already in the inventory.

**You will be asked for:**
- **Item name** – must match an item already added
- **New quantity**
- **New price**

> ⚠️ The item name must match exactly (including capitalisation). If it is not found, an error message will appear.

---

### Option 3 – Update Sold Item

Reduces the stock of an item after a sale.

**You will be asked for:**
- **Item name** – the item that was sold
- **Quantity sold** – must not exceed the current stock

The remaining stock and updated total price are shown after the update.

**Example:**
```
Enter the name of the item sold: Pen
Enter quantity sold: 10
10 Pen(s) sold. Remaining stock: 40
```

---

### Option 4 – Display All Items

Shows a table of all current inventory items.

**Example output:**
```
Current Inventory:
Name           Quantity  Price     Total Price
--------------------------------------------------
Pen            40        1.50      60.00
Ruler          20        0.80      16.00
```

> If the inventory is empty, the message `No items in inventory.` will be shown.

---

### Option 5 – Save to CSV

Saves all inventory data to a file called `inventory.csv` in the same folder as the program.

The CSV file contains these columns:

| Name | Quantity | Price | Total Price |
|---|---|---|---|
| Pen | 40 | 1.5 | 60.00 |

You can open `inventory.csv` with Microsoft Excel or Google Sheets.

> If the inventory is empty, nothing will be saved and a message will appear.

---

### Option 6 – View Insights

Displays four automatic insights about your inventory:

| Insight | Description |
|---|---|
| 🏆 Highest stock value item | The item with the highest total price (quantity × price) |
| ⚠️ Lowest stock item | The item with the least quantity remaining |
| 💰 Total inventory value | The combined worth of all items in stock |
| 📊 Average price per item | The average unit price across all items |

---

## 🔒 Input Rules

The program will reject invalid inputs and ask you to try again.

| Field | What is allowed | What is rejected |
|---|---|---|
| Item name | Letters and spaces only (e.g. `Pen`, `Glue Stick`) | Numbers, empty input (e.g. `123`, `P3n`) |
| Quantity | Whole numbers only, 0 or more | Decimals, letters, negative numbers |
| Price | Decimal or whole numbers, 0 or more | Letters, negative numbers |
| Quantity sold | Positive whole number, not more than current stock | 0, negative, more than available stock |
| Menu option | Numbers 1 to 6 | Anything else |

---

## 🧪 Example Walkthrough

Here is a simple test run to try after launching the program:

1. Enter **1** → Add `Pen`, quantity `100`, price `$0.50`
2. Enter **1** → Add `Ruler`, quantity `30`, price `$1.20`
3. Enter **4** → View the inventory table
4. Enter **3** → Sell `20` units of `Pen`
5. Enter **6** → View insights
6. Enter **5** → Save to `inventory.csv`
7. Enter **n** → Exit the program

---

## 👤 Author

**catandc0m3-del**
GitHub: [catandc0m3-del/Programminggg-2-Individuual-Project](https://github.com/catandc0m3-del/Programminggg-2-Individuual-Project)
