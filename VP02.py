# Задача 1: Подсчет количества чисел, содержащих цифру 3
count = 0
for i in range(1, 2025):
    if '3' in str(i):
        count += 1
print("Количество чисел от 1 до 2024, содержащих цифру 3:", count)
# Задача 2: Сжатие строки
def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))  # Добавляем последний символ и счетчик
    return ''.join(compressed)
# Пример использования
input_string = "aabcccccaaa"
compressed_string = compress_string(input_string)
print("Сжатая строка:", compressed_string)
# Задача 3: Шифр Цезаря
def caesar_cipher(text, shift, decrypt=False):
    result = []
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            result.append(new_char)
        else:
            result.append(char)  # Добавляем символы, не являющиеся буквами, без изменений

    return ''.join(result)
# Пример использования
text = "Hello, World!"
shift = 3
# Шифрование
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)
# Дешифрование
decrypted_text = caesar_cipher(encrypted_text, shift, decrypt=True)
print("Дешифрованный текст:", decrypted_text)
