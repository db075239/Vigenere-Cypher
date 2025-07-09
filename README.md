# Vigenere Cipher Implementation and Cryptanalysis

This repository contains Python implementations of the Vigenere cipher for both encryption and decryption, and a cryptanalysis tool to break Vigenere-encrypted messages using the Kasiski method and frequency analysis.

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Files](#files)
* [Vigenere Cipher (Projekt.py)](#vigenere-cipher-projektpy)
    * [How it Works](#how-it-works)
    * [Usage](#usage)
* [Vigenere Cipher Cryptanalysis (KeyLengths.py & DodatnaNaloga.py)](#vigenere-cipher-cryptanalysis-keylengths.py--dodatnanalogapy)
    * [Kasiski Method](#kasiski-method)
    * [Frequency Analysis for Key Recovery](#frequency-analysis-for-key-recovery)
    * [Usage](#usage-1)
* [Results](#results)
* [References](#references)

## Introduction

The Vigenere cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a form of polyalphabetic substitution cipher, offering more security than a simple Caesar cipher by making frequency analysis more difficult. This project provides a robust implementation of the Vigenere cipher, capable of handling both text and binary files, along with a cryptanalysis tool that leverages the Kasiski method and frequency analysis to determine the key length and subsequently decrypt the ciphertext.

## Features

* **Vigenere Cipher (`Projekt.py`)**:
    * Encrypts and decrypts text input from the keyboard.
    * Encrypts and decrypts binary files.
    * Supports custom code tables for text-based encryption/decryption.
    * Secure key input (password masked).
* **Vigenere Cipher Cryptanalysis (`KeyLengths.py`, `DecryptText.py`)**:
    * **Kasiski Method**: Analyzes ciphertext to suggest possible key lengths by finding repeating patterns and calculating their greatest common divisors. 
    * **Frequency Analysis**: Recovers the Vigenere key for a given key length by analyzing the most common characters in segments of the ciphertext. 
    * Decrypts a Vigenere-encrypted file based on the determined key length.

## Files

* `Projekt.py`: The main Vigenere cipher implementation for encryption and decryption of text and binary files.
* `KeyLengths.py`: Implements the Kasiski method to suggest possible key lengths for a Vigenere ciphertext.
* `DecryptText.py`: Contains functions to find the Vigenere key using frequency analysis and to decrypt the ciphertext once the key length is known.
* `tajnopis`: An example encrypted file used for cryptanalysis.
* `Vaja2bTabela.txt`: A code table used by `Projekt.py` for text encryption/decryption.
* `Izbirni projekt - David Blazheski.pdf`: The project report (in Slovene), detailing the implementation and results.

## Vigenere Cipher (`Projekt.py`)

### How it Works

The `Projekt.py` script provides a universal Vigenere cipher function that can encrypt or decrypt data. [cite: 107]

* **Text Encryption/Decryption**: When a code table is provided, the function operates on text. Each character in the plaintext is associated with a numerical code from the table. [cite: 114] The shift for each character is calculated based on its numerical code and the corresponding character in the key. [cite: 115] For encryption, the character's code is increased by the key character's code, and for decryption, it's decreased. [cite: 116, 117] The result is then mapped back to a character using a reverse code table. [cite: 92, 97]
* **Binary Data Encryption/Decryption**: If no code table is provided, the function treats the input as binary data. [cite: 112, 118] Each byte in the data is shifted by the corresponding byte in the key using modular arithmetic (modulo 256) for encryption or decryption. [cite: 102, 104, 119]

The core Vigenere cipher operations use modular arithmetic:
* Encryption: $C_{i}=(M_{i}+K_{i}) \pmod{26}$ [cite: 63]
* Decryption: $M_{i}=(C_{i}-K_{i}) \pmod{26}$ [cite: 65]
where $M$ is the message, $C$ is the ciphertext, and $K$ is the key. [cite: 68]

### Usage

To run `Projekt.py`:

1.  Execute the script: `python Projekt.py`
2.  Choose between text encryption/decryption (1) or file encryption/decryption (2). [cite: 134]
    * **For Text (1)**:
        * Enter the text to be encrypted. [cite: 126]
        * Enter the key (input is masked for security). [cite: 127, 70]
        * The encrypted and decrypted text will be displayed. [cite: 128]
    * **For Files (2)**:
        * Enter the input file name (e.g., `sifrirana.png.vig`). [cite: 135]
        * Choose how to input the key: from a file (1) or directly via keyboard (2). [cite: 136]
        * Enter the mode (`encrypt` or `decrypt`). [cite: 137]
        * Enter the output file name (e.g., `desifrirana.png`). [cite: 138]
        * If key from file, enter the key file name (e.g., `kljuc.vig`). [cite: 139]
        * The operation status will be displayed. [cite: 140]

## Vigenere Cipher Cryptanalysis (`KeyLengths.py` & `DodatnaNaloga.py`)

This section describes the tools used to break a Vigenere cipher, specifically the `tajnopis` file.

### Kasiski Method

The Kasiski method is employed to determine the most probable key length. [cite: 148] It works by:
1.  **Finding Repeating Patterns**: Identifying sequences of characters (typically 3 or more) that appear multiple times in the ciphertext. [cite: 149]
2.  **Calculating Distances**: Measuring the distances between the occurrences of these repeating patterns. [cite: 149]
3.  **Finding Common Divisors**: The greatest common divisors (GCDs) of these distances are calculated. [cite: 150] The most frequently occurring GCDs are strong indicators of the key length. [cite: 151]

As per the analysis in `Izbirni projekt - David Blazheski.pdf`, the Kasiski method suggested 113 as the most probable key length for `tajnopis` with a frequency of 45352. [cite: 152, 153]

### Frequency Analysis for Key Recovery

Once the key length is determined, frequency analysis is used to recover the actual key. The ciphertext is divided into `key_length` segments, where each segment contains characters that were encrypted with the same key character. [cite: 184] By finding the most common character in each segment and comparing it to the most common character in the expected plaintext (e.g., space character in Slovenian text), individual key bytes can be deduced. [cite: 185]

### Usage

To perform cryptanalysis on the `tajnopis` file:

1.  **Determine Key Length (`KeyLengths.py`)**:
    * Run `KeyLengths.py`. This script will automatically read the `tajnopis` file and print suggested key lengths.
    * `python KeyLengths.py`
    * The output will show a list of suggested key lengths and their frequencies, for example: `Suggested key lengths: [(113, 45352), (2, 22782), ...]`. [cite: 152]
    * Based on the highest frequency, identify the most likely key length (e.g., 113). [cite: 153]

2.  **Decrypt Ciphertext (`DodatnaNaloga.py`)**:
    * Edit `DodatnaNaloga.py` and ensure the `key_length` variable is set to the determined key length (e.g., `key_length = 113`). [cite: 225]
    * Run `DodatnaNaloga.py`. This script will use the Kasiski method's suggested key length to find the key and decrypt `tajnopis`.
    * `python DodatnaNaloga.py`
    * The decrypted text will be saved to `decrypted_cipher.txt`. [cite: 220, 228]
    * A message confirming the decryption will be printed: `"Vaše besedilo je v datoteki decrypted_cipher.txt"` (Your text is in the file decrypted_cipher.txt). [cite: 221, 222]

## Results

The Vigenere cipher implementation (`Projekt.py`) was tested for both text and file encryption/decryption, demonstrating correct functionality. [cite: 131] For instance, encrypting "David Blazheski Projekt pri predmetu IK.!" with the key "kodi" successfully yielded and then decrypted the text. [cite: 130, 128] File decryption was also demonstrated with a `.png.vig` file decrypted using a key from `kljuc.vig` to produce `desifrirana.png`. [cite: 142, 143]

The cryptanalysis tools successfully identified the key length of 113 for the `tajnopis` file, which contains the original text "Med dvema stoloma" by Josip Jurčič. [cite: 153, 229] The decrypted text was saved to `decrypted_cipher.txt`. [cite: 228]

## References

* [1] Wikipedia contributors. (2025, January 11). Vigenere cipher. In *Wikipedia, The Free Encyclopedia*. Retrieved from https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Friedman_test [cite: 231]
* [2] National Cipher Challenge 2024. (2025, January 11). Five ways to crack vigenere cipher. https://www.cipherchallenge.org/wp-content/uploads/2020/12/Five-ways-to-crack-a-Vigenere-cipher.pdf [cite: 233, 234, 235, 236]
