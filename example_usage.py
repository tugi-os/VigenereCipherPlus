# example_usage.py

from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

def main():
    # Example 1: Encrypting and decrypting a simple text
    plaintext = "helloworld"
    keyword = "earth"
    
    print("Original text:", plaintext)
    print("Keyword:", keyword)
    
    # Encrypt the plaintext
    encrypted_text = vigenere_encrypt(plaintext, keyword)
    print("Encrypted text:", encrypted_text)
    
    # Decrypt the encrypted text
    decrypted_text = vigenere_decrypt(encrypted_text, keyword)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
