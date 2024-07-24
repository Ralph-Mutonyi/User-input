shopping_list = ["apples", "bread", "milk", "eggs", "cheese"]

# print the list
print(shopping_list)

#print the first item
print(shopping_list[0])

# print the last item
print(shopping_list[-1])

# print slice of the list from second to the fourth item
print(shopping_list[1:4])

# add a new item to the end of the list
shopping_list + ["bananas"]

# Remove an item from the list
del shopping_list[3]

# check if a specific item is in the list and print a boolean result
print("eggs" in shopping_list) # True
print("butter" in shopping_list) # False

# create a list of prices(floats) corresponding to each item in the shopping list
prices = [1.99, 2.99, 3.99, 4.99, 5.99]

# Calculate the total cost of the items in the shopping list
total_cost = sum(prices)
print("Total cost: $",)