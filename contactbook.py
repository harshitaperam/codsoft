import json
import os

class Contact:
    """Class representing a contact."""
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        """Convert contact to dictionary format for JSON."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Contact instance from a dictionary."""
        return cls(data['name'], data['phone'], data['email'])

class ContactBook:
    """Class representing a contact book."""
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Contact.from_dict(contact) for contact in data]
        return []

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def add_contact(self, name, phone, email):
        """Add a new contact."""
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(contact.to_dict())

    def search_contact(self, name):
        """Search for a contact by name."""
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact.to_dict())
        else:
            pri
