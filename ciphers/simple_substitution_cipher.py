import random
import sys

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    message = input("Enter message: ")
    key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    resp = input("Encrypt/Decrypt [e/d]: ")

    check_valid_key(key)

    if resp.lower().startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif resp.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)

    print(f"\n{mode.title()}ion: \n{translated}")


def check_valid_key(key: str) -> None:
    """
    # Bad Key
    >>> check_valid_key("LFWOAYUISVKMNXPBDCRJTQEGHZ")
    >>> try:
    ...     check_valid_key("G"*26)
    ... except SystemExit as e:
    ...     str(e)
    'Error in the key or symbol set.'
    """
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()

    if key_list != letters_list:
        sys.exit("Error in the key or symbol set.")


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    """
    # Non Letter Pass through and Case Preservation
    >>> ky = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    >>> translate_message(ky, "CjS 5678", "encrypt")
    'WvR 5678'
    >>> translate_message(ky, "19-SJC%%", "decrypt")
    '19-ITR%%'
    """
    translated = ""
    chars_a = LETTERS
    chars_b = key

    if mode == "decrypt":
        chars_a, chars_b = chars_b, chars_a

    for symbol in message:
        if symbol.upper() in chars_a:
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            translated += symbol

    return translated


def get_random_key() -> str:
    """
    # Has to be a permutation of A through Z with no repeats
    >>> rand_key = get_random_key()
    >>> len(rand_key) == 26 and set(rand_key) == set(LETTERS) and len(set(rand_key)) == 26
    True
    """
    key = list(LETTERS)
    random.shuffle(key)
    return "".join(key)


if __name__ == "__main__":
    main()
