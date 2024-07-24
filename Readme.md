# Day 1 Assignment
Project: Shopping List Manager
Create a Python script that manages a shopping list. The script should do the following:

Initialize an empty list called shopping_list.
Create functions to:
a. Add an item to the list
b. Remove an item from the list
c. Display the current list
d. Check if an item is in the list (return a boolean)
e. Get the total number of items
f. Get a slice of the list (e.g., first 3 items)
g. Calculate the total cost of items (assume each item has a price)
Use a mix of strings (for item names), floats (for prices), and integers (for quantities) in your list items.
Implement a simple menu system that allows the user to perform these operations.

Here's a starting point for your script:
pythonCopyshopping_list = []

def add_item(item):
    # Your code here

def remove_item(item):
    # Your code here

def display_list():
    # Your code here

def is_item_in_list(item):
    # Your code here

def get_item_count():
    # Your code here

def get_first_n_items(n):
    # Your code here

def calculate_total_cost():
    # Your code here

# Main program
while True:
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display list")
    print("4. Check if item is in list")
    print("5. Get item count")
    print("6. Get first n items")
    print("7. Calculate total cost")
    print("8. Quit")
    
    choice = input("Enter your choice (1-8): ")
    
    # Implement the menu options here
This project will allow you to practice:

Working with lists (adding, removing, checking membership)
Using different data types (strings, ints, floats, booleans)
List operations (slicing, length)
Basic input/output
Control structures (if/else, while loop)
Function definitions and calls
