# Vigenere Cipher Implementation and Cryptanalysis

This repository contains Python implementations of the Vigenere cipher for both encryption and decryption, and a cryptanalysis tool to break Vigenere-encrypted messages using the Kasiski method and frequency analysis.

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Files](#files)
* [Vigenere Cipher (Projekt.py)](#vigenere-cipher-projektpy)
    * [How it Works](#how-it-works)
    * [Usage](#usage)
* [Vigenere Cipher Cryptanalysis (KeyLengths.py & DecryptText.py)](#vigenere-cipher-cryptanalysis-keylengths.py--DecryptTextpy)
    * [Kasiski Method](#kasiski-method)
    * [Frequency Analysis for Key Recovery](#frequency-analysis-for-key-recovery)
    * [Usage](#usage-1)
* [Results](#results)
* [References](#references)

## Introduction

The Vigenere cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a form of polyalphabetic substitution cipher, offering more security than a simple Caesar cipher by making frequency analysis more difficult. This project provides a robust implementation of the Vigenere cipher, capable of handling both text and binary files, along with a cryptanalysis tool that leverages the Kasiski method and frequency analysis to determine the key length and subsequently decrypt the ciphertext.

## Features

* **Vigenere Cipher (`Projekt.py`)**:
    * Encrypted and decrypted text input from the keyboard.
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
* `tajnopis`: A Vigenere-encrypted text file that needs to be cracked without prior knowledge of the key. Its decryption involves first finding the key length using the Kasiski method and then applying frequency analysis.
* `šifrirana.png.vig`: A Vigenere-encrypted PNG image file.
* `kljuc.vig`: The key file used to decrypt `šifrirana.png.vig`.
* `Vaja2bTabela.txt`: A code table used by `Projekt.py` for text encryption/decryption.
* `Izbirni projekt - David Blazheski.pdf`: The project report (in Slovene), detailing the implementation and results.

## Vigenere Cipher (`Projekt.py`)

### How it Works

The `Projekt.py` script provides a universal Vigenere cipher function that can encrypt or decrypt data[cite: 107].

* **Text Encryption/Decryption**: When a code table is provided, the function operates on text. Each character in the plaintext is associated with a numerical code from the table. The shift for each character is calculated based on its numerical code and the corresponding character in the key. For encryption, the character's code is increased by the key character's code, and for decryption, it's decreased. The result is then mapped back to a character using a reverse code table.
* **Binary Data Encryption/Decryption**: If no code table is provided, the function treats the input as binary data. In this case, for each byte in the data, the corresponding shift from the key is applied (added or subtracted) using modular arithmetic (modulo 256) for encryption or decryption.

The core Vigenere cipher operations can be represented with modular arithmetic (assuming A=0, B=1, ..., Z=25):
* Encryption: $C_{i}=E_{K}(M_{i})=(M_{i}+K_{i}) \pmod{26}$ [cite: 63]
* Decryption: $M_{i}=D_{K}(C_{i})=(C_{i}-K_{i}) \pmod{26}$ [cite: 65]
where $M=M_{1}...M_{n}$ is the message, $C=C_{1}...C_{n}$ is the ciphertext, and $K=K_{1}...K_{n}$ is the key, obtained by repeating a keyword $\lceil n/m\rceil$ times, where $m$ is the length of the keyword.

### Usage

To run `Projekt.py`:

1.  Execute the script: `python Projekt.py`
2.  Choose between text encryption/decryption (1) or file encryption/decryption (2).
    * **For Text (1)**:
        * Enter the text to be encrypted.
        * Enter the key (input is masked for security).
        * The encrypted and decrypted text will be displayed.
    * **For Files (2)**:
        * Enter the input file name (e.g., `šifrirana.png.vig`).
        * Choose how to input the key: from a file (1) or directly via keyboard (2).
        * Enter the mode (`encrypt` or `decrypt`).
        * Enter the output file name (e.g., `desifrirana.png`).
        * If key from file, enter the key file name (e.g., `ključ.vig`).
        * The operation status will be displayed.

## Vigenere Cipher Cryptanalysis (`KeyLengths.py` & `DecryptText.py`)

This section describes the tools used to break a Vigenere cipher, specifically the `tajnopis` file.

### Kasiski Method

The Kasiski method is employed to determine the most probable key length. It works by:
1.  **Finding Repeating Patterns**: Identifying sequences of characters (typically 3 or more) that appear multiple times in the ciphertext.
2.  **Calculating Distances**: Measuring the distances between the occurrences of these repeating patterns.
3.  **Finding Common Divisors**: The greatest common divisors (GCDs) of these distances are calculated. The most frequently occurring GCDs are strong indicators of the key length.

As per the analysis in `Izbirni projekt - David Blazheski.pdf`, the Kasiski method suggested 113 as the most probable key length for `tajnopis`, having the highest frequency of occurrence (45352).

### Frequency Analysis for Key Recovery

Once the key length is determined, frequency analysis is used to recover the actual key. The ciphertext is divided into `key_length` segments, where each segment contains characters that were encrypted with the same key character. By finding the most common character (e.g., the space character, which is one of the most common in Slovenian texts) in each segment and comparing it to the value of a common character, individual key bytes can be deduced.

### Usage

To perform cryptanalysis on the `tajnopis` file:

1.  **Determine Key Length (`KeyLengths.py`)**:
    * Run `KeyLengths.py`. This script will automatically read the `tajnopis` file and print suggested key lengths.
    * `python KeyLengths.py`
    * The output will show a list of suggested key lengths and their frequencies, for example: `Suggested key lengths: [(113, 45352), (2, 22782), ...]`.
    * Based on the highest frequency, identify the most likely key length (e.g., 113).

2.  **Decrypt Ciphertext (`DecryptText.py`)**:
    * Edit `DecryptText.py` and ensure the `key_length` variable is set to the determined key length (e.g., `key_length = 113`).
    * Run `DecryptText.py`. This script will read the encrypted data, calculate the key using the `find_key` function, decrypt the text using the `decrypt` function, and save the decrypted text to `decrypted_cipher.txt`.
    * `python DecryptText.py`
    * The decrypted text will be saved to `decrypted_cipher.txt`.
    * A message confirming the decryption will be printed: `"Vaše besedilo je v datoteki decrypted_cipher.txt"` (Your text is in the file decrypted_cipher.txt).

## Results

The Vigenere cipher implementation (`Projekt.py`) was tested for both text and file encryption/decryption, demonstrating correct functionality. For instance, encrypting "David Blazheski Projekt pri predmetu IK.!" with the key "kodi" successfully yielded and then decrypted the text. File decryption was also demonstrated with a `sifrirana.png.vig` file decrypted using a key from `kljuc.vig` to produce `desifrirana.png`.

The cryptanalysis tools successfully identified the key length of 113 for the `tajnopis` file, which contains the original text "Med dvema stoloma" by Josip Jurčič. The decrypted text was saved to `decrypted_cipher.txt`.

## References

* [1] Wikipedia contributors. (2025, January 11). Vigenere cipher. In *Wikipedia, The Free Encyclopedia*. Retrieved from https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Friedman_test
* [2] National Cipher Challenge 2024. (2025, January 11). Five ways to crack vigenere cipher. https://www.cipherchallenge.org/wp-content/uploads/2020/12/Five-ways-to-crack-a-Vigenere-cipher.pdf
