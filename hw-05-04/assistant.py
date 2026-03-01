from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        for p in self.phones:
            if phone == p.value:
                self.phones.remove(p)
                return

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if old_phone == p.value:
                p.value = Phone(new_phone).value
                return
    def find_phone(self, phone):
        for p in self.phones:
            if phone == p.value:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record
    def find(self, name):
        return self.data[name]
    def delete(self, name):
        del self.data[name]



book = AddressBook()
print(book)
john_record = Record("John")
print(john_record.name)
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print(john_record)
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")