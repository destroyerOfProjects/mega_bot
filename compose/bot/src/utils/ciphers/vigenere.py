def get_message_and_key_for_work(message: str, key: str) -> tuple[str, str]:
    key *= len(message) // len(key) + 1
    return message, key.upper()


def encryption(message: str, key: str) -> str:
    message, key = get_message_and_key_for_work(message=message, key=key)
    encrypted_message = ''
    for index, char in enumerate(message):
        if char.isupper():
            gg = (ord(char) - ord('A')) + (ord(key[index]) - ord('A'))
            encrypted_message += chr(gg % 26 + ord('A'))
        elif char.islower():
            gg = (ord(char) - ord('a')) + (ord(key[index]) - ord('A'))
            encrypted_message += chr(gg % 26 + ord('a'))
        else:
            encrypted_message += char

    return encrypted_message


def decryption(message: str, key: str) -> str:
    message, key = get_message_and_key_for_work(message=message, key=key)
    decrypted_message = ''
    for index, char in enumerate(message):
        if char.isupper():
            gg = (ord(char) - ord('A')) - (ord(key[index]) - ord('A'))
            decrypted_message += chr(gg % 26 + ord('A'))
        elif char.islower():
            gg = (ord(char) - ord('a')) - (ord(key[index]) - ord('A'))
            decrypted_message += chr(gg % 26 + ord('a'))
        else:
            decrypted_message += char
    return decrypted_message
