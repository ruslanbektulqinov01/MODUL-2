import sqlite3
import sys

from prettytable import PrettyTable


class ContactsRepository:
    def __init__(self, db):
        self.db = db

    def add_contact(self, first_name, last_name, phone_number):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO contacts (first_name, last_name, phone_number)
            VALUES (?, ?, ?)
            """,
            (first_name, last_name, phone_number)
        )
        db.commit()

    def get_contacts(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT * FROM contacts
            """
        )
        return cursor.fetchall()

    def get_contact_by_name(self, first_name):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT * FROM contacts
            WHERE first_name = ?
            """,
            (first_name,)
        )
        return cursor.fetchall()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python exercise_1 only one argument")

    available_commands = ("add_contact", "get_contacts", "get_contact_by_name")
    command = sys.argv[1]

    if command not in available_commands:
        sys.exit(f"Invalid command: {command}\n available commands: {available_commands}")

    with sqlite3.connect("contacts.db") as db:
        repository = ContactsRepository(db)
        if command == "add_contact":
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            phone_number = input("Enter the phone number: ")
            repository.add_contact(first_name, last_name, phone_number)
            print("Contacts added")
        elif command == "get_contacts":
            contacts = repository.get_contacts()
            table = PrettyTable(["First Name", "Last Name", "Phone Number"])
            for contact in contacts:
                table.add_row(contact)
            print(table)
        elif command == "get_contact_by_name":
            first_name = input("Enter the first name: ")
            contacts = repository.get_contact_by_name(first_name)
            table = PrettyTable(["First Name", "Last Name", "Phone Number"])
            for contact in contacts:
                table.add_row(contact)
            print(table)
