#Display Greeting to include separator
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Seabrooks Luxury Auto Mall")
print("Please complete our   form to build your vehicle")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print()

#Display Make and Model choices
print("AVAILABLE MODELS")
print("Which vehicle are you interested in?")
print("a. Poor Man Putt Around")
print("b. Working Man Car")
print("c. Supervisor Sedan")
print("d. Manager Mobile")
print("e. Executive Exclusive")
ModelChoice = input("Please enter a-e: ")
print()
print(f"User Chose:  {ModelChoice} ")
print()
print()

#User chooses Trim of Model - X or LX
print("UPGRADE TRIM")
print("Would you like to upgrade to the LX Model?")
Trim = input(f"Yes or No:   ")
print()
print(f"Upgrade {Trim} ")

#User chooses Exterior Color
print()
print("PLEASE CHOOSE COLOR")
Color = input(f"Please enter color choice: ")
print()
print(f"User wants {ModelChoice} in {Color}")
print()
print()

#User chooses Entertainment Pkg
print("PLEASE CHOOSE ENTERTAINMENT PACKAGE")
print()
print("a. Standard")
print("b. Upgraded")
print("c. Premium Surround")
print()
EntPgk = input("Please enter a-c: ")
print(f"User would like Ent Pkg {EntPgk}")
print()
print()

#User chooses extended warranty coverage - mult choice
print("PLEASE CHOOSE EXTENDED WARRANTY OPTION")
print()
print("a. None")
print("b. 60,000")
print("c. 100,000")
print()
Warranty = input("Please enter a-c: ")
print(f"User Chooses Warranty {Warranty}")
print()
print()

#Summary
print("=====================================================")
print("SUMMARY OF VEHICLE BUILD")
print()
print(f"Model Option {ModelChoice}")
print(f"Model Choice {ModelChoice}")
print(f"Color choice {Color}")
print(f"Choice of Entertainment Pacage was {EntPgk}")
print(f"Customer wants {Warranty}")
print(
  "Thank you for your selection, we will contact you when your vehicle is available.  Thank your for shopping Seabrooks Luxury Auto Mall"
)
print("=====================================================")
