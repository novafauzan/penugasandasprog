#Nama : Fauzan Fuadiansyah 
#NIM : J0403231085
#Email : novamarsfauzan@apps.ipb.ac.id

#Format Loop
#while test:			# Loop test
#    statements		# Loop body
#    if test: break 	# Exit loop now, skip else if present
#    if test: continue 	# Go to top of loop now, to test1
#else:
#    statements 		# Run if we didn't hit a 'break'

#Iteration variable
favorites = ['Churros', 'Tiramisú', 'Pudding']
count = 0		# count is iteration variable
while count < len(favorites):
    print('One of my favorite desserts is', favorites[count]);
    count += 1

#Examples - Infinite Loop
while True:  #constant condition
    print("This is an infinite loop")

#Example - Avoid Infinite Loop using Proper Condition, User Input & Break
text = input('masukkan sebuah huruf : ')
while text != "q":										
    text = input("Please enter a chemical formula (or 'q' to exit): ")	
    if text == "q":
        print("…exiting program")
        Break											
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

#For loop example 
favorites = ['Churros', 'Tiramisú', 'Pudding']
for dessert in favorites:
    print('One of my favorite desserts is', dessert)

#Loop pattern 
country = 'Republik Indonesia'
for ch in country:
    print(ch, end=' ')

#Counting
survey_responses = ["positive", "neutral", "positive", "negative", "positive", "positive", "neutral"]

positive_count = 0

for response in survey_responses:
    if response == "positive":
        positive_count += 1

print(f"Number of positive responses: {positive_count}")

#Summing
sales_transactions = [100.50, 75.25, 50.75, 30.00, 45.50]

total_revenue = 0

for transaction in sales_transactions:
    total_revenue += transaction

print(f"Total revenue: ${total_revenue:.2f}")

#Filtering
email_addresses = ["user1@spam.com", "user2@gmail.com", "user3@spam.com"]

spam_emails = []

for email in email_addresses:
    if email.endswith("@spam.com"):
        spam_emails.append(email)		

print("Spam emails:")
for email in spam_emails:
    print(email)

#Searching
student_names = ["Alice", "Bob", "Charlie", "David"]
student_name_to_search = "Charlie"

student_found = False

for name in student_names:
    if name == student_name_to_search:
        student_found = True
        break

if student_found:
    print(f"Student {student_name_to_search} found.")
else:
    print(f"Student {student_name_to_search} not found.")

#Finding Maximum/Minimum
temperatures = [75, 82, 79, 88, 91, 84, 77]
max_temperature = temperatures[0]

for temperature in temperatures:
    if temperature > max_temperature:
        max_temperature = temperature

print(f"The maximum temperature of the week was {max_temperature}°F.")

#Range()Function 
import time

countdown_seconds = 5

print("Get ready for liftoff!")
for remaining_seconds in range(countdown_seconds, 0, -1):
    print(f"{remaining_seconds}...")
    time.sleep(1)

print("Blast off!")

#Nesting Loops
height = 5  # Height of the pyramid

for i in range(1, height + 1):
    # Print spaces before the stars
    for j in range(height - i):
        print(" ", end="")

    # Print the stars
    for k in range(2 * i - 1):
        print("*", end="")

    # Move to the next line after each row
    print()

#Controlling loop with else 
favorites = ['Churros', 'Tiramisú', 'Pudding']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert) 
else:
    print('No sorry, that dessert is not on my list')

#Controlling loop with break 
favorites = ['Churros', 'Tiramisú', 'Pudding']

for dessert in favorites:
    if dessert == 'Pudding':
        print('My favorite is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')

#Continue in loops
snacks_in_stock = ["chips", "candy", "soda", "cookies"]
user_choice = ""

while user_choice != "q":
    user_choice = input("Enter your snack choice (or 'q' to exit): ")

    # Check if the user wants to quit
    if user_choice == "q":
        print("Thank you for using the vending machine.")
        break

    # Check if the selected snack is in stock
    if user_choice not in snacks_in_stock:
        print("Sorry, that snack is not available.")
        continue  # Continue iteration without dispensing the snack

    # Dispense the selected snack
    print(f"Dispensing {user_choice}. Enjoy your snack!")

print("Vending machine session ended.")

#Pass in loops
valid_login = "admin"
valid_password = "password"

while True:
    login = input("Enter your login: ")
    password = input("Enter your password: ")

    if login == valid_login and password == valid_password:
        print("Authentication successful!")
        break
    else:
        print("Invalid credentials. Please try again.")
        pass  # Placeholder for later (e.g., account lockout)

print("Welcome, admin!")

