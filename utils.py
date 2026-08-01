def print_header(title):
    """
    Print a formatted section header.
    """
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def get_float(prompt):
    """
    Keep asking until the user enters a valid positive number.
    """
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Amount cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_non_empty_input(prompt):
    """
    Keep asking until the user enters non-empty text.
    """
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_int(prompt):
    """
    Keep asking until the user enters a valid integer.
    """
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("Please enter a valid integer.")


def confirm_action(message):
    """
    Ask the user for confirmation.
    Returns True if user enters Y.
    """
    while True:
        choice = input(f"{message} (Y/N): ").strip().upper()

        if choice == "Y":
            return True

        if choice == "N":
            return False

        print("Please enter Y or N.")