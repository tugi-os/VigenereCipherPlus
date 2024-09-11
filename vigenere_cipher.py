import random

def is_vowel(char):
    """
    Checks if the character is a vowel.

    Parameters:
    char (str): A single character.

    Returns:
    bool: True if the character is a vowel, False otherwise.
    """
    return char.lower() in 'aeiou'

def apply_random_shift(char, shift_amount):
    """
    Applies a random shift to a character with the given shift amount.

    Parameters:
    char (str): The character to be shifted.
    shift_amount (int): The amount to shift.

    Returns:
    str: The shifted character.
    """
    return chr((ord(char) + shift_amount - ord('a')) % 26 + ord('a'))

def extend_keyword(keyword, length):
    """
    Extends the keyword to match the length of the plaintext.

    Parameters:
    keyword (str): The keyword used for encryption/decryption.
    length (int): The length of the text to be encrypted/decrypted.

    Returns:
    str: The extended keyword.
    """
    extended = (keyword * (length // len(keyword))) + keyword[:length % len(keyword)]
    return extended.lower()

def vigenere_encrypt(plaintext, keyword):
    """
    Encrypts the plaintext using the Vigenère Cipher with additional random shifts for vowels.

    Parameters:
    plaintext (str): The text to be encrypted.
    keyword (str): The keyword used for encryption.

    Returns:
    str: The encrypted text (ciphertext).
    """
    keyword = extend_keyword(keyword, len(plaintext))
    encrypted_text = ""

    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = keyword[i]

        if char.isalpha():  # Only encrypt alphabetic characters
            shift = ord(key_char.lower()) - ord('a')  # Calculate the shift amount
            
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            # Apply random shift if the character is a vowel
            if is_vowel(shifted_char):
                shift_amount = random.randint(1, 5)  # Generate a random integer between 1 and 5
                if shifted_char.isupper():
                    shifted_char = apply_random_shift(shifted_char.lower(), shift_amount).upper()
                else:
                    shifted_char = apply_random_shift(shifted_char, shift_amount)
            else:
                shift_amount = 0  # No additional shift for non-vowels
            
            encrypted_text += shifted_char + str(shift_amount)  # Add character and shift amount
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged

    return encrypted_text

def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypts the ciphertext using the Vigenère Cipher with random shifts.

    Parameters:
    ciphertext (str): The text to be decrypted.
    keyword (str): The keyword used for decryption.

    Returns:
    str: The decrypted text (original plaintext).
    """
    keyword = extend_keyword(keyword, len(ciphertext) // 2)  # Adjust for shift digits
    decrypted_text = ""

    i = 0
    while i < len(ciphertext):
        char = ciphertext[i]
        if char.isalpha():
            key_char = keyword[len(decrypted_text)]
            shift = ord(key_char.lower()) - ord('a')  # Retrieve keyword shift
            
            # Retrieve shift amount (next character is a digit or 0)
            if i + 1 < len(ciphertext) and ciphertext[i + 1].isdigit():
                shift_amount = int(ciphertext[i + 1])
                i += 2  # Move past the character and the shift amount
            else:
                shift_amount = 0
                i += 1  # Move past only the character if no shift digit
            
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift - shift_amount + 26) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift - shift_amount + 26) % 26 + ord('a'))
        else:
            decrypted_text += char
            i += 1

    return decrypted_text

if __name__ == "__main__":
    print("Welcome to the Vigenère Cipher Implementation with Random Vowel Shifts!")
    plaintext = input("Enter the text to encrypt: ")
    keyword = input("Enter the keyword: ")
    
    encrypted = vigenere_encrypt(plaintext, keyword)
    print("\nEncrypted text:", encrypted)
    
    decrypted = vigenere_decrypt(encrypted, keyword)
    print("Decrypted text:", decrypted)
