from typing import Dict

CONTACTS: Dict[str, str] = {}


def parse_input(user_input: str) -> tuple[str, list[str]]:

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args: list[str]) -> str:

    name, phone = args
    CONTACTS[name] = phone
    return "Contact added."


def change_contact(args: list[str]) -> str:

    name, phone = args
    if name not in CONTACTS:
        return "Contact not found."

    CONTACTS[name] = phone
    return "Contact updated."


def show_phone(name: str) -> str:

    if name not in CONTACTS:
        return "Contact not found."

    return CONTACTS[name]


def show_all() -> None:

    for name, phone in CONTACTS.items():
        print(f"{name}: {phone}")


def main():

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args))

        elif command == "change":
            print(change_contact(args))

        elif command == "phone":
            print(show_phone(args[0]))

        elif command == "all":
            show_all()

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
