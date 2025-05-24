class Reservation:
    def __init__(self, number, date, time, name, adults, children):
        self.number = number
        self.date = date.title()
        self.time = time
        self.name = name.title()
        self.adults = adults
        self.children = children

    # Calculate subtotal
    def subtotal(self):
        return (self.adults * 500) + (self.children * 300)

    # Format to display rows
    def display_rows(self, show_subtotal=False):  # Hide subtotal from rows unless report is generated
        if show_subtotal:
          subtotal = f"{self.subtotal()}"
        else:
          subtotal = ''
        return (f'{self.number:<10}{self.date:<20}{self.time:<15}{self.name:<20}'
                f'{self.adults:<10}{self.children:<15}{subtotal}')

class ReservationSystem:
    def __init__(self):
        # Predefined list of reservations
        self.reservations = [
            Reservation(1, 'Nov 10, 2020', '10:00 am', 'John Doe', 1, 1),
            Reservation(2, 'Nov 25, 2020', '11:00 am', 'Michelle Franks', 2, 1),
            Reservation(3, 'Dec 10, 2020', '9:00 am', 'Ella Flich', 2, 2),
            Reservation(4, 'Dec 21, 2020', '12:00 pm', 'Dylan Cloze', 1, 2),
        ]
    # Read reservations
    def view_reservation(self, show_subtotal=False):
        columns = ['#', 'Date', 'Time', 'Name', 'Adults', 'Children']
        width = [10, 20, 15, 20, 10, 15, 15]  # Width spacing for columns
        if show_subtotal:
            columns.append('Subtotal')  # Show subtotal in columns if report is generated
        print(''.join(f'{columns[i]:<{width[i]}}' for i in range(len(columns))))  # Print columns with spacing
        for reservation in self.reservations:
            print(reservation.display_rows(show_subtotal))  # Method call to print rows

    # Error handling for creating reservation
    def handle_input(self, prompt, is_integer=False):
        while True:
            user_input = input(prompt).strip()
            if is_integer:
                try:
                    value = int(user_input)
                    if value < 0:  # When user input is negative
                        print('Value cannot be negative. Please enter a valid number.')
                        continue
                    return value
                except ValueError:  # Handle case when user input is not a valid integer
                    print('Please enter a valid integer.')
            else:
                if user_input:  # Check for non-empty string
                    return user_input
                print('This field cannot be empty. Please enter a valid value.')

    # Create reservations
    def make_reservation(self):
        number = len(self.reservations) + 1  # Assign new reservation number
        name = self.handle_input('Name: ')
        date = self.handle_input('Date: ')
        time = self.handle_input('Time: ')
        adults = self.handle_input('No. of adults: ', is_integer=True)
        children = self.handle_input('No. of children: ', is_integer=True)
        # Append user input to existing reservation list
        self.reservations.append(Reservation(number, date, time, name, adults, children))
        print('\nReservation made successfully!')

    # Delete reservations
    def delete_reservation(self):
        # Check if the reservations list is empty
        if not self.reservations:
            print('\nNo reservations available to delete.')
            return
        user_input = input('Enter reservation number to delete: ')
        # Error handling
        try:
            number = int(user_input)
            # Remove the reservation from the list
            if 1 <= number <= len(self.reservations):
                del self.reservations[number - 1]
                # Update reservation numbers after deletion
                for i in range(number - 1, len(self.reservations)):
                    self.reservations[i].number -= 1
                print('\nReservation deleted successfully!')
            else:
                print('\nInvalid reservation number.')
        except ValueError:
            print('\nPlease enter a valid integer for the reservation number.')

    # Generate report
    def generate_report(self):
        print('REPORT\n'.center(100))
        # Method call + show subtotal in columns and rows
        self.view_reservation(show_subtotal=True)

        # Calculate total number of adults, kids, and amount
        total_adults = sum(reservation.adults for reservation in self.reservations)
        total_children = sum(reservation.children for reservation in self.reservations)
        grand_total = sum(reservation.subtotal() for reservation in self.reservations)

        # Display total number of adults, kids, and amount
        print(f'\nTotal number of adults: {total_adults}')
        print(f'Total number of kids: {total_children}')
        print(f'Grand Total: PHP {grand_total:.2f}')
        print('-' * 41 + ' nothing follows ' + '-' * 41)

    # Display menu options
    def display_menu(self):
        print('\nRESTAURANT RESERVATION SYSTEM')
        print('System Menu')
        print('a. View all Reservations')
        print('b. Make Reservation')
        print('c. Delete Reservation')
        print('d. Generate Report')
        print('e. Exit')

    # Execute program
    def run(self):
        while True:
            self.display_menu()
            choice = input('\nEnter your choice: ').lower()
            print()

            if choice == 'a':
                self.view_reservation()
            elif choice == 'b':
                self.make_reservation()
            elif choice == 'c':
                self.delete_reservation()
            elif choice == 'd':
                self.generate_report()
            elif choice == 'e':
                print('Thank you!')
                break
            else:
                print('Invalid option.')

reservation_system = ReservationSystem()
reservation_system.run()