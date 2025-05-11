import json
import os
from typing import List, Dict

class ContactBook:
    def __init__(self):
        self.contacts: List[Dict] = []
        self.data_file = "contacts.json"
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.contacts = json.load(f)

    def save_contacts(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self):
        print("\nAdd New Contact")
        contact = {
            "name": input("Name: ").strip(),
            "phone": input("Phone: ").strip(),
            "email": input("Email: ").strip(),
            "address": input("Address: ").strip()
        }

        if not contact["name"] or not contact["phone"]:
            print("Name and Phone are required!")
            return
            
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact saved successfully!")

    def display_contacts(self):
        if not self.contacts:
            print("\nContact book is empty!")
            return
            
        print("\nContact List:")
        print("-"*60)
        print(f"{'No.':<5} | {'Name':<20} | {'Phone':<15} | Email")
        print("-"*60)
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx:<5} | {contact['name'][:20]:<20} | {contact['phone'][:15]:<15} | {contact['email']}")

    def search_contacts(self):
        term = input("\nSearch (name/phone): ").lower().strip()
        results = [
            c for c in self.contacts
            if term in c["name"].lower() or term in c["phone"]
        ]
        
        if not results:
            print("No matching contacts found!")
            return
            
        print(f"\nFound {len(results)} matching contacts:")
        for contact in results:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-"*40)

    def edit_contact(self):
        self.display_contacts()
        if not self.contacts:
            return
            
        try:
            index = int(input("\nEnter contact number to edit: ")) - 1
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                print("\nEditing Contact:")
                print(f"1. Name: {contact['name']}")
                print(f"2. Phone: {contact['phone']}")
                print(f"3. Email: {contact['email']}")
                print(f"4. Address: {contact['address']}")
                
                field = int(input("\nChoose field to edit (1-4): "))
                new_value = input("Enter new value: ").strip()
                
                fields = ["name", "phone", "email", "address"]
                if 1 <= field <= 4:
                    contact[fields[field-1]] = new_value
                    self.save_contacts()
                    print("Contact updated successfully!")
                else:
                    print("Invalid field selection!")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number!")

    def delete_contact(self):
        self.display_contacts()
        if not self.contacts:
            return
            
        try:
            index = int(input("\nEnter contact number to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                deleted = self.contacts.pop(index)
                self.save_contacts()
                print(f"Deleted contact: {deleted['name']}")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number!")

def main_menu():
    book = ContactBook()
    
    while True:
        print("\n" + "="*30)
        print("CONTACT BOOK MANAGER")
        print("="*30)
        print("1. View All Contacts")
        print("2. Add New Contact")
        print("3. Search Contacts")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        try:
            choice = int(input("\nChoose option (1-6): "))
            if choice == 1:
                book.display_contacts()
            elif choice == 2:
                book.add_contact()
            elif choice == 3:
                book.search_contacts()
            elif choice == 4:
                book.edit_contact()
            elif choice == 5:
                book.delete_contact()
            elif choice == 6:
                print("\nGoodbye! Contacts saved automatically.")
                break
            else:
                print("Please choose 1-6!")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main_menu()