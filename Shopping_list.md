# Project: Simple Shopping List
# Create a Python script that does the following:

Create a shopping list with at least 5 items. Each item should be a string.
Print the entire list.
Print the first item in the list.
Print the last item in the list.
Print a slice of the list from the second to the fourth item.
Add a new item to the end of the list.
Remove an item from the list.
Check if a specific item is in the list and print a boolean result.
Create a list of prices (floats) corresponding to each item.
Calculate and print the total cost of all items.

Here's a template to get you started:
pythonCopy# 1. Create the shopping list
shopping_list = ["apples", "bread", "milk", "eggs", "cheese"]

# 2. Print the entire list
print("Shopping list:", shopping_list)

# 3. Print the first item
print("First item:", shopping_list[0])

# 4. Print the last item
print("Last item:", shopping_list[-1])

# 5. Print a slice of the list (2nd to 4th item)
print("2nd to 4th items:", shopping_list[1:4])

# 6. Add a new item
shopping_list.append("yogurt")
print("List after adding yogurt:", shopping_list)

# 7. Remove an item
shopping_list.remove("bread")
print("List after removing bread:", shopping_list)

# 8. Check if an item is in the list
is_milk_in_list = "milk" in shopping_list
print("Is milk in the list?", is_milk_in_list)

# 9. Create a list of prices
prices = [1.50, 2.75, 3.25, 2.50, 4.00, 2.00]

# 10. Calculate and print the total cost
total_cost = sum(prices)
print("Total cost: $", total_cost)
This project covers:

Creating and manipulating lists
Using strings and floats
List indexing and slicing
Adding and removing list items
Checking list membership (resulting in a boolean)
Basic list operations (sum)

You can run this code and experiment with it. Try modifying the lists, changing the slice ranges, or adding more operations to further practice these concepts.