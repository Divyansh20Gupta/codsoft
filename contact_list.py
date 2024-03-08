contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully.")

def view_contact_list():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. Name: {contact['name']}, Phone Number: {contact['phone_number']}")

def search_contact():
    search_query = input("Enter contact name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']:
            found_contacts.append(contact)
    if found_contacts:
        print("Search Results:")
        for i, contact in enumerate(found_contacts):
            print(f"{i+1}. Name: {contact['name']}, Phone Number: {contact['phone_number']}")
    else:
        print("No matching contacts found.")

def update_contact():
    search_query = input("Enter contact name or phone number to update: ")
    found_contact = None
    for contact in contacts:
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']:
            found_contact = contact
            break
    if found_contact:
        print("Contact found. Enter new details:")
        found_contact['name'] = input("Enter updated name: ")
        found_contact['phone_number'] = input("Enter updated phone number: ")
        found_contact['email'] = input("Enter updated email: ")
        found_contact['address'] = input("Enter updated address: ")
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    search_query = input("Enter contact name or phone number to delete: ")
    found_contact = None
    for contact in contacts:
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']:
            found_contact = contact
            break
    if found_contact:
        contacts.remove(found_contact)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
