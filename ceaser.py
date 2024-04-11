alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print("The text after encryption is:", cipher_text)


def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print("The text after decryption is:", plain_text)

wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'E' for encryption and 'D' for decryption: ").upper()
    text = input("Type your message: ").lower()
    shift = int(input("Enter shift value: "))

    if what_to_do == "E":
        encryption(text, shift)

    elif what_to_do == "D":
        decryption(text, shift)

    repeat = input("Type 'y' to continue and 'n' to exit: ").upper()
    if repeat == 'N':
        wanna_end = True
        print("Closing!!!")
