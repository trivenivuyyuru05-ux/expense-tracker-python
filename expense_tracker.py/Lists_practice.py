expenses = []

for i in range(3):
    amount = int(input("Enter expense: "))
    expenses.append(amount)

print("All expenses: ", expenses)
print("Total: ", sum(expenses))