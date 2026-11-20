def calculate_total(food, travel, shopping):
    return food + travel + shopping

print("Welcome to my Expense Tracker")

food = int(input("Food expense: "))
travel = int(input("Travel expense: "))
shopping = int(input("Shopping expense: "))

total = calculate_total(food, travel, shopping)

print("Total expense:", total)
