# Алфавиты
RUS_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
RUS_ALPHABET_REVERSE = RUS_ALPHABET[::-1]

# Кодовая таблица для русского: 0-9 и A-W (33 символа)
RUS_CODE_TABLE = "0123456789ABCDEFGHIJKLMNOPQRSTUVW"
RUS_CODE_MAP = {ch: i for i, ch in enumerate(RUS_CODE_TABLE)}

ENG_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENG_ALPHABET_REVERSE = ENG_ALPHABET[::-1]

# Кодовая таблица для английского: 0-9 и A-P (26 символов)
ENG_CODE_TABLE = "0123456789ABCDEFGHIJKLMNOP"
ENG_CODE_MAP = {ch: i for i, ch in enumerate(ENG_CODE_TABLE)}


def encrypt(text: str, language: str):
    """Функция шифрует сообщение и возвращает строку"""
    # Разделение текста на части по последнему пробелу
    parts = text.rsplit(' ', 1)

    if len(parts) != 2:
        return "KEY ERROR"

    text_to_encrypt = parts[0]
    cipher_key_str = parts[1]

    # Проверка ключа
    if cipher_key_str not in ["0", "1"]:
        return "KEY ERROR"

    # Преобразование последней части в число
    cipher_key = int(cipher_key_str)

    # Выбор алфавита и кодового словаря в зависимости от языка и ключа
    if language == "rus":
        if cipher_key == 1:
            alphabet = RUS_ALPHABET  # Прямой
        else:
            alphabet = RUS_ALPHABET_REVERSE  # Обратный
        code_table = RUS_CODE_TABLE
    else:
        if cipher_key == 1:
            alphabet = ENG_ALPHABET
        else:
            alphabet = ENG_ALPHABET_REVERSE
        code_table = ENG_CODE_TABLE

    # Шифрование
    result = []
    for char in text_to_encrypt.upper():
        if char in alphabet:
            index = alphabet.index(char)
            result.append(code_table[index])
        else:
            result.append(char)

    return "".join(result) + cipher_key_str


def decrypt(ciphertext: str, language: str):

    # Последний символ ключ
    key_bit_str = ciphertext[-1]
    if key_bit_str not in ["0", "1"]:
        return "KEY ERROR!"

    key_bit = int(key_bit_str)
    encrypted_part = ciphertext[:-1]

    # Выбор алфавита и кодового словаря
    if language == "rus":
        if key_bit == 1:
            alphabet = RUS_ALPHABET  # Прямой
        else:
            alphabet = RUS_ALPHABET_REV  # Обратный
        code_map = RUS_CODE_MAP
    else:
        if key_bit == 1:
            alphabet = ENG_ALPHABET
        else:
            alphabet = ENG_ALPHABET_REV
        code_map = ENG_CODE_MAP

    # Расшифровка
    result = []
    for char in encrypted_part:
        if char in code_map:
            index = code_map[char]
            if index < len(alphabet):
                result.append(alphabet[index])
            else:
                result.append(char)
        else:
            result.append(char)

    return "".join(result)
