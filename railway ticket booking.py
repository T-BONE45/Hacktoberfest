class RailwayTicketBooking:
    def __init__(self, train_name, total_seats):
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.passenger_list = []

    def book_ticket(self, passenger_name, num_tickets):
        if num_tickets <= self.available_seats:
            self.passenger_list.append((passenger_name, num_tickets))
            self.available_seats -= num_tickets
            print(f"Ticket(s) booked for {passenger_name}: {num_tickets} seat(s) on {self.train_name}.")
        else:
            print(f"Sorry, only {self.available_seats} seat(s) available on {self.train_name}.")

    def cancel_ticket(self, passenger_name):
        for i, (name, num_tickets) in enumerate(self.passenger_list):
            if name == passenger_name:
                self.available_seats += num_tickets
                del self.passenger_list[i]
                print(f"Ticket(s) canceled for {passenger_name}.")
                return
        print(f"No booking found for {passenger_name}.")

    def display_status(self):
        print(f"Train: {self.train_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print("Passenger List:")
        for name, num_tickets in self.passenger_list:
            print(f"{name}: {num_tickets} ticket(s)")

def main():
    train_name = "Sample Train"
    total_seats = 50
    booking_system = RailwayTicketBooking(train_name, total_seats)

    while True:
        print("\nRailway Ticket Booking System")
        print("1. Book a Ticket")
        print("2. Cancel a Ticket")
        print("3. Display Train Status")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            passenger_name = input("Enter passenger name: ")
            num_tickets = int(input("Enter number of tickets to book: "))
            booking_system.book_ticket(passenger_name, num_tickets)
        elif choice == "2":
            passenger_name = input("Enter passenger name to cancel ticket: ")
            booking_system.cancel_ticket(passenger_name)
        elif choice == "3":
            booking_system.display_status()
        elif choice == "4":
            print("Thank you for using the Railway Ticket Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
