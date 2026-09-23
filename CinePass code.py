# --- Dynamic User Input ---
base_price = 15

# Ask the user for data in the terminal
age = int(input("Enter age: "))
seat_type = input("Enter seat type (Premium/Gold/Standard): ")
show_time = input("Enter show time (Evening/Matinee/Morning): ")
day_of_the_week = input("Enter day of the week (e.g., Monday, Sunday): ")

# Dynamically set is_weekend based on day_of_the_week
is_weekend = day_of_the_week in ["Saturday", "Sunday"]
is_member = False  # Keep static or change to input() if needed

# --- Booking Restrictions Logic ---
if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# --- Discount Logic ---
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# --- Extra Charges Logic ---
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# --- Final Ticket Evaluation ---
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = extra_charges + service_charges + base_price - discount
    print('Final price of ticket:', final_price)    
else:
    print('Ticket booking failed due to restrictions')
