"""
HIT137 - Assignment 2
Question 1: Text Encryption & Decryption System

Student: Suraj Devkota
Student ID: S397467
Date: December 2026

Description:
This program reads a text file (raw_text.txt), encrypts the text using a 
reversible Caesar cipher, saves it, then decrypts it back and verifies the result.
It uses absolute paths so it works from any folder.
"""

import os

# Absolute paths for all files
BASE_FOLDER = "/Users/surajdevkota/Desktop/HIT137_ASSIGNMENT2"
RAW_TEXT_FILE = os.path.join(BASE_FOLDER, "raw_text.txt")
ENCRYPTED_FILE = os.path.join(BASE_FOLDER, "encrypted_text.txt")
DECRYPTED_FILE = os.path.join(BASE_FOLDER, "decrypted_text.txt")


def encrypt_text(shift):
    """Encrypts raw text using a simple Caesar shift"""
    if not os.path.exists(RAW_TEXT_FILE):
        print(f"❌ ERROR: RAW TEXT file not found at {RAW_TEXT_FILE}")
        return False

    with open(RAW_TEXT_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    encrypted = ""
    for char in text:
        if char.islower():
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted += char

    with open(ENCRYPTED_FILE, "w", encoding="utf-8") as file:
        file.write(encrypted)

    print(f"✅ Encryption complete! Saved to: {ENCRYPTED_FILE}")
    return True


def decrypt_text(shift):
    """Decrypts encrypted text using the same Caesar shift"""
    if not os.path.exists(ENCRYPTED_FILE):
        print(f"❌ ERROR: Encrypted file not found at {ENCRYPTED_FILE}")
        return False

    with open(ENCRYPTED_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    decrypted = ""
    for char in text:
        if char.islower():
            decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
        elif char.isupper():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted += char

    with open(DECRYPTED_FILE, "w", encoding="utf-8") as file:
        file.write(decrypted)

    print(f"✅ Decryption complete! Saved to: {DECRYPTED_FILE}")
    return True


def verify_decryption():
    """Compares RAW_TEXT_FILE and DECRYPTED_FILE to verify correctness"""
    if not os.path.exists(RAW_TEXT_FILE) or not os.path.exists(DECRYPTED_FILE):
        print("❌ Verification failed: required files are missing.")
        return

    with open(RAW_TEXT_FILE, "r", encoding="utf-8") as f1, \
         open(DECRYPTED_FILE, "r", encoding="utf-8") as f2:
        if f1.read() == f2.read():
            print("✅ Decryption successful: Files match exactly!")
        else:
            print("❌ Decryption failed: Files do not match!")


def main():
    print("=" * 60)
    print("TEXT ENCRYPTION & DECRYPTION SYSTEM")
    print("=" * 60)

    # Get shift value from user
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("❌ Invalid input! Please enter an integer.")
        return

    print(f"\nUsing shift: {shift}\n")

    print("-" * 60)
    print("STEP 1: ENCRYPTION")
    print("-" * 60)
    if not encrypt_text(shift):
        return

    print("\nSTEP 2: DECRYPTION")
    print("-" * 60)
    if not decrypt_text(shift):
        return

    print("\nSTEP 3: VERIFICATION")
    print("-" * 60)
    verify_decryption()

    print("\nAll files generated in folder:")
    print(f"  - {RAW_TEXT_FILE} (original)")
    print(f"  - {ENCRYPTED_FILE} (encrypted)")
    print(f"  - {DECRYPTED_FILE} (decrypted)")


if __name__ == "__main__":
    main()
