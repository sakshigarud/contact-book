class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"{name} already exists in the contact book.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact {name} added successfully.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} removed successfully.")
        else:
            print(f"{name} does not exist in the contact book.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the contact book.")
        else:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(
                    f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            contact_book.add_contact(name, phone, email)
        elif choice == "2":
            name = input("Enter the name to remove: ")
            contact_book.remove_contact(name)
        elif choice == "3":
            contact_book.display_contacts()
        elif choice == "4":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
