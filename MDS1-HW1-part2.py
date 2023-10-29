CONTACTS = {}

def parse_input(user_input):
    user_input = user_input.split()
    command = user_input[0].lower()
    args = user_input[1:] if len(user_input) > 1 else []
    return command, args

def add_contact(name, phone):
    if name in CONTACTS:
        return f"Contact for {name} already exists"
    elif len(phone) == 0:
        return "Please provide a name and phone"
    else:
        CONTACTS[name] = phone
        return f"Contact added: {name}, {phone}"

def change_contact(name, phone):
    if name in CONTACTS:
        CONTACTS[name] = phone
        return f"Contact updated: {name}, {phone}"
    else:
        return f"No contact found for {name}"

def show_phone(name):
    if name in CONTACTS:
        return f"Phone for {name}: {CONTACTS[name]}"
    else:
        return f"No contact found for {name}"

def show_all():
    if not CONTACTS:
        return "No contacts found"
    else:
        result = "All contacts:\n"
        for name, phone in CONTACTS.items():
            result += f"{name}: {phone}\n"
        return result

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            result = add_contact(*args)
            print(result)

        elif command == "change":
            result = change_contact(*args)
            print(result)

        elif command == "phone":
            result = show_phone(*args)
            print(result)

        elif command == "all":
            result = show_all()
            print(result)

        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
