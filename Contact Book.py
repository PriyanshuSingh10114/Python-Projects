"""TASK 5-CONTACT BOOK"""

"""Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.
"""

class Contact:
    def __init__(self, name, phone_no, email, address):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if any(c.email.lower() == contact.email.lower() for c in self.contacts):
            print("Email already exists in the contact book.")
            return
        self.contacts.append(contact)
        print("Contact added successfully in the contact book.")


    def view_contacts(self):
        if not self.contacts:
            print("No contacts available in the contact book.")
            return
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_no}, Email: {contact.email}, Address: {contact.address}")


    def search_contact(self, search):
        search = search.lower()
        found_contacts = [
            contact for contact in self.contacts
            if search in contact.name.lower() or search in contact.phone_no.lower() or search in contact.email.lower()]
        if found_contacts:
            print("\nContacts found:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_no}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No contacts found in the contact book.")


    def update_contact(self, name, new_phone_no, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_email.lower() != contact.email.lower() and any(c.email.lower() == new_email.lower() for c in self.contacts):
                    print("Email already exists in the contact book.")
                    return
                contact.phone_no = new_phone_no
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully in the contact book.")
                return
        print("Contact not found in the contact book.")


    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully in the contact book.")
                return
        print("Contact not found in the contact book.")


def get_contact_details():
    name = input("Enter your name: ")
    phone_no = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone_no, email, address)


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Book")
        print("Enter 1 to Add Contact")
        print("Enter 2 to View Contacts")
        print("Enter 3 to Search Contact")
        print("Enter 4 to Update Contact")
        print("Enter 5 to Delete Contact")
        print("Enter 6 to Exit")

        choice = input("Enter your choice (1-6) : ")

        if choice =='1':
            contact = get_contact_details()
            contact_manager.add_contact(contact)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            search = input("Enter name or phone to search: ")
            contact_manager.search_contact(search)
        elif choice == '4':
            name = input("Enter the name of the contact you want to update: ")
            new_phone_no = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone_no, new_email, new_address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")

if __name__ == "__main__":
    main()









        




 






        
