def vernam_encrypt(plaintext: str, key: str) -> str:
    """
    >>> vernam_encrypt("HELLO","KEY")
    'RIJVS'
    >>> vernam_encrypt("ZAGREUS", "HADES")
    'GAJVWBS'
    >>> vernam_encrypt("", "BLANK") # empty plaintext
    ''
    >>> vernam_encrypt("X", "E") # wrap-around
    'B'
    >>> vernam_encrypt("CRYPTOGRAPHY", "NDA") # key shorter than text
    'PUYCWOTUACKY'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        ct = ord(key[i % len(key)]) - 65 + ord(plaintext[i]) - 65
        while ct > 25:
            ct = ct - 26
        ciphertext += chr(65 + ct)
    return ciphertext


def vernam_decrypt(ciphertext: str, key: str) -> str:
    """
    >>> vernam_decrypt("RIJVS","KEY")
    'HELLO'
    >>> vernam_decrypt("GAJVWBS", "HADES")
    'ZAGREUS'
    >>> vernam_decrypt("", "BLANK")
    ''
    >>> vernam_decrypt("B", "E")
    'X'
    >>> m, k = "CRYPTOGRAPHY", "NDA"
    >>> vernam_decrypt(vernam_encrypt(m, k), k) == m
    True
    """
    decrypted_text = ""
    for i in range(len(ciphertext)):
        ct = ord(ciphertext[i]) - ord(key[i % len(key)])
        while ct < 0:
            ct = 26 + ct
        decrypted_text += chr(65 + ct)
    return decrypted_text


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Example usage
    plaintext = "HELLO"
    key = "KEY"
    encrypted_text = vernam_encrypt(plaintext, key)
    decrypted_text = vernam_decrypt(encrypted_text, key)
    print("\n\n")
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
