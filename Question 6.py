values = []
for i in range(5):
    num = float(input(f"Enter value{i+1}:"))
    values.append(num)

average = sum(values)/ len(values)
print("The average of the entered values =",average)    