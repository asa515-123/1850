# Worksheet 1.2: Task 1 Solution
import sys
try:
    grade=int(input("please enter grade:"))
except ValueError:
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit()
if not (0<=grade<=100):
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit()
if 0<=grade<=39:
    print(f"{grade} is a fail")
elif 40<=grade<=69:
    print(f"{grade} is a pass")
elif 70<=grade<=100:
    print(f"{grade} is a distinction")
