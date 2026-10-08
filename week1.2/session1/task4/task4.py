# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#tomato
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#because of .union it mixes both sets
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("halwa omaniya")
print(fruit)
# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)
# Find and display symmetric difference of the two sets
aj=fruit.symmetric_difference(vegetables)
print(aj)