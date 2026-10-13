# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
if not numbers:
    print("Error: no numbers provided",file=sys.stderr)
    sys.exit(1)


numbers_sorted=sorted(numbers)
n = len(numbers)
mid = n//2
if n % 2==1:
    median=(numbers_sorted[mid])
else:
    median=(numbers_sorted[mid-1]+numbers_sorted[mid])/2
lowest=min(numbers)
highest=max(numbers)
mean=sum(numbers)/len(numbers)
print(f"Minimum = {lowest}")
print(f"Maximum = {highest}")
print(f"Mean = {mean}")
print(f"Median = {median}")