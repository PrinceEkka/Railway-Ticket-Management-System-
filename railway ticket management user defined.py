import pandas as pd
import random

# Sample train data (replace with actual data)
train_data = {
    "Train": ["Shatabdi Express", "Rajdhani Express", "Garib Rath", "Duronto Express"],
    "Sleeper Seats": [100, 150, 200, 120],
    "AC Seats": [50, 75, 60, 40],
    "Sleeper Price": [500, 700, 300, 600],
    "AC Price": [1200, 1500, 800, 1000]
}

trains = pd.DataFrame(train_data)

# Function to check seat availability
def check_availability(train, class_type, num_seats):
    if train in trains["Train"].values:
        index = trains[trains["Train"] == train].index[0]
        if class_type == "Sleeper":
            if trains.loc[index, 'Sleeper Seats'] >= num_seats:
                return True
            else:
                return False
        elif class_type == 'AC':
            if trains.loc[index, 'AC Seats'] >= num_seats:
                return True
            else:
                return False
        else:
            print("Invalid class type.")
            return False
    else:
        print("Train not found.")
        return False

# Function to book tickets
def book_tickets(train, class_type, num_seats):
    if check_availability(train, class_type, num_seats):
        index = trains[trains['Train'] == train].index[0]
        if class_type == 'Sleeper':
            trains.loc[index, 'Sleeper Seats'] -= num_seats
            price = trains.loc[index, 'Sleeper Price']
        elif class_type == 'AC':
            trains.loc[index, 'AC Seats'] -= num_seats
            price = trains.loc[index, 'AC Price']
        pnr_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
        print("\nTickets booked successfully!")
        print("PNR Number:", pnr_number)
        print("Total fare:", price * num_seats)
    else:
        print("\nBooking failed. Seats not available.")

# User-defined menu
def main():
    while True:
        print("\n--- Train Ticket Booking System ---")
        print("1. Check Seat Availability")
        print("2. Book Tickets")
        print("3. View Updated Train Availability")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            train_name = input("Enter the train name: ")
            class_type = input("Enter class type (Sleeper/AC): ")
            num_seats = int(input("Enter number of seats: "))
            available = check_availability(train_name, class_type, num_seats)
            if available:
                print("\nSeats are available.")
            else:
                print("\nSeats are not available.")
        elif choice == '2':
            train_name = input("Enter the train name: ")
            class_type = input("Enter class type (Sleeper/AC): ")
            num_seats = int(input("Enter number of seats: "))
            book_tickets(train_name, class_type, num_seats)
        elif choice == '3':
            print("\nUpdated Train Availability:\n", trains)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
main()
