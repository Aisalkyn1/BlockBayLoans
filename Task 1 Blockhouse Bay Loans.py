# Program to calculate total due and the instalments payable on a loan.

instalments = [3, 6, 9, 12]


# Function to calculate loan instalments
def loaninstalments():
    i = r / n
    numerator = P * i * (1 + i) ** n
    denominator = (1 + i) ** n - 1
    instalment = numerator / denominator
    return instalment


# Function to calculate total due amount of loan
def totaldue():
    totalpayment = loaninstalments() * n
    return totalpayment


try:
    P = float(input("Please enter loan amount rounded to 2 decimal places: "))
except ValueError:
    print("Invalid input. Try Again!")
    P = float(input("Please enter loan amount rounded to 2 decimal places: "))

while P < 1000.00 or P > 10000.00 or 4999.99 < P < 5000:
    print("\nWrong loan amount. Please enter value, rounded to 2 decimal places, between 1000 and 10000 inclusive.")
    try:
        P = float(input("Please enter loan amount rounded to 2 decimal places: "))
    except ValueError:
        print("Invalid input. Try Again!")
        P = float(input("Please enter loan amount rounded to 2 decimal places: "))

try:
    n = float(input("\nPlease enter number of instalments (3, 6, 9, or 12 per year): "))
except ValueError:
    print("Invalid input. Try Again!")
    n = float(input("\nPlease enter number of instalments (3, 6, 9, or 12 per year): "))

while n not in instalments:
    print("\nWrong instalment number.")
    try:
        n = float(input("\nPlease enter number of instalments (3, 6, 9, or 12 per year): "))
    except ValueError:
        print("Invalid input. Try Again!")
        n = float(input("\nPlease enter number of instalments (3, 6, 9, or 12 per year): "))

if 1000 <= P <= 4999.99:
    r = 0.1
    loaninstalments()
    totaldue()
    print("\nTotal due loan amount will be $" + str(round(totaldue(), 2)) + " paid in " + str(
        int(n)) + " instalments of $" + str(round(loaninstalments(), 2)) + ".")

elif 5000.00 <= P <= 10000.00:
    r = 0.08
    loaninstalments()
    totaldue()
    print("\nTotal due loan amount will be $" + str(round(totaldue(), 2)) + " paid in " + str(
        int(n)) + " instalments of $" + str(round(loaninstalments(), 2)) + ".")
else:
    print("Invalid input.")

input("\nPress any key to continue.")
