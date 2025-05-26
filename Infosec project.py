# Write a program that asks the user for a number of days. The program then prints out the number of seconds in the number of days given.

days = int(input("Enter the number of days: "))
seconds = days * 24 * 60 * 60
print(f"There are {seconds} seconds in {days} day(s).")



