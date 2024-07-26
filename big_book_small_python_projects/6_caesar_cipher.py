"""
The Caesar cipher is an ancient encryption
algorithm used by Julius Caesar. It
encrypts letters by shifting them over by a
certain number of places in the alphabet. We
call the length of shift the key. For example, if the
key is 3, then A becomes D, B becomes E, C becomes
F, and so on. To decrypt the message, you must shift
the encrypted letters in the opposite direction. This
program lets the user encrypt and decrypt messages
according to this algorithm.

"""

CIPHER_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                  "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def encrypt(key, plain_text):
    encrypted_list = []

    for s in plain_text:
        if s == " ":
            encrypted_list.append(" ")
        else:
            S = s.upper()
            s_value = CIPHER_VALUES.index(S)
            new_S_value = (s_value + key) % 26
            encrypted_list.append(CIPHER_VALUES[new_S_value])
    return "".join(encrypted_list)


def decrypt(key, encrypted_text):
    decrypted_list = []

    for e in encrypted_text:
        if e == " ":
            decrypted_list.append(" ")
        else:
            E = e.upper()
            e_value = CIPHER_VALUES.index(E)
            new_E_value = abs(26 + e_value - key) % 26
            decrypted_list.append(CIPHER_VALUES[new_E_value])
    return "".join(decrypted_list)


def main():
    print("Do you want to encrypt or decrypt- e/d")
    action = input()

    if action not in ["e", "d"]:
        print("You can either encrypt or decrypt")
        exit(1)
    
    print("Enter the key(0 to 25) to use")
    key_str = input()
    key = 0
    try:
        key = int(key_str)
    except ValueError:
        print("Please enter valid number for key. Exiting")
        exit(1)
    
    if action == "e":
        print("Enter the message to encrypt")
        plain_text = input()
        encrypted_text = encrypt(key, plain_text)
        print(f"Encrypted text is: {encrypted_text}")
    else:
        print("Enter the message to decrypt")
        encrypted_text = input()
        decrypted_text = decrypt(key, encrypted_text)
        print(f"Decrypted text is: {decrypted_text}")


if __name__ == "__main__":
    main()


def test_encrypt():
    assert encrypt(1, "A") == "B"
    assert encrypt(2, "A") == "C"
    assert encrypt(1, "Z A") == "A B"
    assert encrypt(2, "A Z Y") == "C B A"


def test_decrypt():
    assert decrypt(1, "B") == "A"
    assert decrypt(2, "C") == "A"
    assert decrypt(1, "A B") == "Z A"
    assert decrypt(2, "C B A") == "A Z Y"