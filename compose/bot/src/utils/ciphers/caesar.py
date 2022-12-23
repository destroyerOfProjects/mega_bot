def encryption(text: str, shift: int) -> str:
    encrypted_message = ''
    for char in text:
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char

    return encrypted_message


def decryption(text: str, shift: int) -> str:
    return encryption(text=text, shift=-shift)


def decryption_with_frequency_analysis(text: str) -> str:
    frequency = count_frequency(text=text)
    common_letter = get_common_letter(letters_frequency=frequency)

    # По статистике, самая часто встречаемая буква в английском языке - E
    most_common_letter = 'e'

    shift = abs(ord(most_common_letter) - ord(common_letter))

    if ord(most_common_letter) > ord(common_letter):
        shift *= -1

    return decryption(text=text, shift=shift)


def count_frequency(text: str) -> dict[str, float]:
    text = clear_text_for_frequency_analyze(text=text)

    count_letters = {chr(i): 0 for i in range(97, 123)}
    for char in text:
        if char not in count_letters.keys():
            count_letters[char] = 0
        count_letters[char] += 1

    for key, value in count_letters.items():
        count_letters[key] = value / len(text)

    return count_letters


def clear_text_for_frequency_analyze(text: str) -> str:
    new_text = ''
    for char in text:
        if char.isalpha():
            new_text += char

    return new_text.lower()


def get_common_letter(letters_frequency: dict[str, float]) -> str:
    mx = 0
    common_letter = ''
    for letter, frequency in letters_frequency.items():
        if frequency > mx:
            mx = frequency
            common_letter = letter

    return common_letter
