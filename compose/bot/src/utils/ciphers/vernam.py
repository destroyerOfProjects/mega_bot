from random import SystemRandom

system_random = SystemRandom()


def encryption(message: str) -> tuple[str, list[int]]:
    full_key = []
    encrypted_message = ''
    for char in message:
        shift = system_random.randint(0, 25)
        full_key.append(shift)

        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char

    return encrypted_message, full_key


def decryption(message: str, key: list[int]) -> str:
    if len(message) != len(key):
        raise ValueError('Key does not match the length of the message')

    decrypted_message = ''
    for index, char in enumerate(message):
        if char.isupper():
            decrypted_message += chr((ord(char) - key[index] - 65) % 26 + 65)
        elif char.islower():
            decrypted_message += chr((ord(char) - key[index] - 97) % 26 + 97)
        else:
            decrypted_message += char

    return decrypted_message
