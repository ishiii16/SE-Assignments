# Name: Ishika Jain | SRN: PES2UG24AM067
# Fixed version: every function checks its input and returns None when it
# is invalid, instead of crashing or returning a wrong value.

DIGITS = "0123456789"


def is_whole_number(text):
    """True only for a non-empty string of the plain digits 0-9."""
    return text != "" and all(ch in DIGITS for ch in text)


def mask_card_number(number):
    """
    Hides all but the last four digits of a card number.
    Returns None unless the input has 12 to 19 digits (spaces and dashes allowed).
    """
    if not isinstance(number, str):
        return None
    digits = number.replace(' ', '').replace('-', '')
    if not is_whole_number(digits) or not 12 <= len(digits) <= 19:
        return None
    return '*' * 12 + digits[-4:]


def parse_transaction(line):
    """
    Parses 'date,category,amount' into a (category, amount) tuple.
    Returns None unless there are exactly three fields, the category is not
    empty and the amount is a positive whole number.
    """
    if not isinstance(line, str):
        return None
    parts = line.split(',')
    if len(parts) != 3:
        return None
    category = parts[1].strip().lower()
    amount = parts[2].strip()
    if category == "" or not is_whole_number(amount) or int(amount) == 0:
        return None
    return category, int(amount)


def parse_statement_total(text):
    """
    Reads the amount from a line such as 'Total: 12,500'.
    Returns None unless there is a colon followed by a whole number.
    """
    if not isinstance(text, str) or ':' not in text:
        return None
    amount = text.split(':', 1)[1].replace(',', '').strip()
    if not is_whole_number(amount):
        return None
    return int(amount)


def show(label, result, error):
    print(label, result if result is not None else error)


def main():
    print("==== Running mask_card_number ====")
    value = input("Enter a card number (e.g. 4111 1111 1111 1234): ")
    show("Masked card number:", mask_card_number(value), "Invalid card number")

    print("\n==== Running parse_transaction ====")
    value = input("Enter a transaction as DATE,CATEGORY,AMOUNT (e.g. 2026-11-05,dining,1550): ")
    show("Category and amount:", parse_transaction(value), "Invalid transaction")

    print("\n==== Running parse_statement_total ====")
    value = input("Enter the statement total line (e.g. Total: 12,500): ")
    show("Statement total:", parse_statement_total(value), "Invalid statement total")


if __name__ == "__main__":
    main()
