import string


def ceasar_cipher_encrypt(s, key):
    cipher = []
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    ALPHABET_LENGTH = len(lowercase_letters)
    for char in s:
        if char in lowercase_letters:
            substitute_index = (lowercase_letters.index(char) + key) % ALPHABET_LENGTH
            cipher.append(lowercase_letters[substitute_index])
        elif char in uppercase_letters:
            substitute_index = (uppercase_letters.index(char) + key) % ALPHABET_LENGTH
            cipher.append(uppercase_letters[substitute_index])
        else:
            cipher.append(char)
    return ''.join(cipher)

def ceasar_cipher_decrypt(s, key):
    # Reverse sign on the key
    key = 0 - key
    return ceasar_cipher_encrypt(s, key)

if __name__ == '__main__':
    clear_text = "Hello, World!"
    key = 3
    cipher_text = ceasar_cipher_encrypt(clear_text, key)
    print(cipher_text)
    print(ceasar_cipher_decrypt(cipher_text, key))