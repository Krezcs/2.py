from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass
    
    @abstractmethod
    def display_notes(self, notes):
        pass
    
    @abstractmethod
    def display_commands(self, commands):
        pass

class ConsoleUI(UserInterface):
    def display_contacts(self, contacts):
        for contact in contacts:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")
    
    def display_notes(self, notes):
        for note in notes:
            print(f"Title: {note['title']}\nContent: {note['content']}\n")
    
    def display_commands(self, commands):
        print("Available commands:")
        for command in commands:
            print(command)



ui = ConsoleUI()
contacts = [
    {
        'name': 'John Doe',
        'phone': '1234567890',
        'email': 'johndoe@example.com'
    },
    {
        'name': 'Jane Smith',
        'phone': '0987654321',
        'email': 'janesmith@example.com'
    }
]
notes = [
    {
        'title': 'Meeting',
        'content': 'Remember to bring the presentation slides.'
    },
    {
        'title': 'Grocery List',
        'content': 'Milk, eggs, bread, and fruits.'
    }
]
commands = [
    'add_contact',
    'delete_contact',
    'view_contacts',
    'add_note',
    'delete_note',
    'view_notes'
]

ui.display_contacts(contacts)
ui.display_notes(notes)
ui.display_commands(commands)