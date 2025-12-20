
while True:
        print("\n--- EVENT PLATFORM ---")
        print("1. Organizer Menu\n2. Staff (Check-in)\n3. Attendee Menu\n4. Exit")
        role = input("Select Role: ")

        if role == '1': 
            print("\n1. Create Event\n2. View Reports\n3. Backup Data")
            choice = input("Choice: ")
            if choice == '1':
                name = input("Event Name: ")
                cap = int(input("Capacity: "))
                price = float(input("Price: "))
