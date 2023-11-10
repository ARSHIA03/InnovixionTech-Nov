class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.contact_id_counter = 1

    def add_contact(self, name, phone, email):
        contact_id = self.contact_id_counter
        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts[contact_id] = contact
        self.contact_id_counter += 1
        print(f"Contact added successfully! Contact ID: {contact_id}")

    def edit_contact(self, contact_id, name=None, phone=None, email=None):
        if contact_id in self.contacts:
            contact = self.contacts[contact_id]
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            print(f"Contact {contact_id} updated successfully!")
        else:
            print(f"Contact ID {contact_id} not found.")

    def delete_contact(self, contact_id):
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            print(f"Contact {contact_id} deleted successfully!")
        else:
            print(f"Contact ID {contact_id} not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact_id, contact in self.contacts.items():
                print(f"ID: {contact_id}, Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def get_user_input(prompt):
    return input(prompt).strip()


def main():
    contact_manager = ContactManager()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = get_user_input("Enter your choice (1-5): ")

        if choice == '1':
            name = get_user_input("Enter name: ")
            phone = get_user_input("Enter phone number: ")
            email = get_user_input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)

        elif choice == '2':
            contact_id = int(get_user_input("Enter contact ID to edit: "))
            name = get_user_input("Enter new name (leave blank to keep current): ")
            phone = get_user_input("Enter new phone number (leave blank to keep current): ")
            email = get_user_input("Enter new email address (leave blank to keep current): ")
            contact_manager.edit_contact(contact_id, name, phone, email)

        elif choice == '3':
            contact_id = int(get_user_input("Enter contact ID to delete: "))
            contact_manager.delete_contact(contact_id)

        elif choice == '4':
            contact_manager.display_contacts()

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
