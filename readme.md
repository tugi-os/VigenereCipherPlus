# Vigenère Cipher with Random Vowel Shifts

## Project Overview

This project features a custom implementation of the Vigenère Cipher, enhanced with additional random shifts applied specifically to vowel characters. It was developed as part of a learning exercise in cryptography, with the aid of AI tools to design and refine the code. The project aims to explore advanced encryption techniques and understand the complexities involved in generating and decrypting cipher text.

## Features

- **Vigenère Cipher Encryption**: Encrypts text using a keyword with the standard Vigenère Cipher technique.
- **Random Vowel Shifts**: Introduces random shifts (between 1 and 5 positions) to vowel characters, adding an extra layer of complexity to the encryption.
- **Decryption**: Accurately decrypts the text using the same keyword and recorded shift values.
- **Shift Amount Recording**: Records the random shift amounts for vowels and appends them to the encrypted text to ensure accurate decryption.

## Motivation

The primary motivation behind this project was to gain deeper insights into cryptography by experimenting with and enhancing classical cipher algorithms. Using AI tools to support various aspects of the coding process allowed me to focus on understanding core cryptographic principles while integrating innovative features like random vowel shifts.

## How It Works

1. **Encryption**:
   - The plaintext is encrypted using the Vigenère Cipher method.
   - Random shifts are applied to vowel characters, resulting in a unique cipher text each time, even with identical input.
   - The shift amounts are recorded and appended to the end of the cipher text for use during decryption.

2. **Decryption**:
   - The original text is recovered by using the keyword and applying the recorded random shift values to reverse the vowel shifts and the Vigenère Cipher.

## Example Usage

For detailed usage examples, refer to the `examples/` folder.

### Encryption Example

In the `examples/example_usage.py` file, you can find example code for encrypting text.

### Decryption Example

In the `examples/example_usage.py` file, you can also find example code for decrypting text.

## Installation

To use this project, clone the repository and run the script:

```bash
git clone https://github.com/tugi-os/vigenere-cipher-random-shifts.git
cd vigenere-cipher-random-shifts
python vigenere_cipher.py
