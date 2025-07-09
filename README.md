# 🔐 Vigenère Cipher Implementation and Cryptanalysis

This repository provides Python implementations for:
- **Vigenère Cipher encryption/decryption**, supporting both text and binary files.
- **Cryptanalysis tools** to crack Vigenère-encrypted messages using the **Kasiski method** and **frequency analysis**.

---

## 📑 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Files](#files)
- [Vigenère Cipher (`Projekt.py`)](#vigenère-cipher-projektpy)
  - [How it Works](#how-it-works)
  - [Usage](#usage)
- [Cryptanalysis (`KeyLengths.py` & `DecryptText.py`)](#cryptanalysis-keylengthspy--decrypttextpy)
  - [Kasiski Method](#kasiski-method)
  - [Frequency Analysis](#frequency-analysis)
  - [Usage](#usage-1)
- [Results](#results)
- [References](#references)

---

## 🧠 Introduction

The **Vigenère cipher** is a polyalphabetic substitution cipher that uses a keyword to apply a series of Caesar ciphers across the text. This makes frequency analysis significantly more difficult than with monoalphabetic ciphers.

This project includes:
- A robust implementation of the cipher that works on both text and binary files.
- Cryptanalysis tools that use **Kasiski examination** and **frequency analysis** to deduce the key and decrypt ciphertext without knowing the original key.

---

## 🚀 Features

### Vigenère Cipher (`Projekt.py`)
- Encrypts and decrypts **text** and **binary files**.
- Supports **custom code tables** for text operations.
- Password input is masked for security.
- Interactive CLI menu for choosing between text or file operations.

### Cryptanalysis Tools (`KeyLengths.py`, `DecryptText.py`)
- **Kasiski Method**: Suggests likely key lengths by analyzing repeated patterns and computing GCDs.
- **Frequency Analysis**: Recovers the key by analyzing letter frequencies in key-length-separated segments.
- Automatic decryption once key is inferred.

---

## 📁 Files

- `Projekt.py`: Main script for Vigenère cipher encryption/decryption (text & binary).
- `KeyLengths.py`: Finds possible key lengths using the Kasiski method.
- `DecryptText.py`: Recovers the key via frequency analysis and decrypts the ciphertext.
- `tajnopis`: A text file encrypted with the Vigenère cipher.
- `šifrirana.png.vig`: Encrypted binary PNG file.
- `kljuc.vig`: Key file used to decrypt the PNG image.
- `Vaja2bTabela.txt`: Custom code table for text operations.
- `Izbirni projekt - David Blazheski.pdf`: Slovene project report detailing implementation and results.

---

## 🔧 Vigenère Cipher (`Projekt.py`)

### How it Works

The script handles both text and binary encryption modes:

- **Text Mode**: Uses a code table to map characters to numbers. Each character is shifted using the corresponding character in the key (modulo table size).
- **Binary Mode**: Performs modular addition/subtraction on bytes (modulo 256).

Mathematical Formulation:
- **Encryption**: `Cᵢ = (Mᵢ + Kᵢ) mod 26`
- **Decryption**: `Mᵢ = (Cᵢ - Kᵢ) mod 26`

Where `M` is plaintext, `C` is ciphertext, and `K` is the repeated key.

### Usage

To run:

```bash
python Projekt.py
```

Then choose:
1. **Text mode**:
   - Enter text.
   - Enter the key (input is hidden).
   - Encrypted and decrypted text will be shown.
2. **File mode**:
   - Enter input/output filenames.
   - Choose to enter the key via file or keyboard.
   - Select `encrypt` or `decrypt`.
   - File operation status will be displayed.

---

## 🕵️ Cryptanalysis (`KeyLengths.py` & `DecryptText.py`)

These tools are used to crack encrypted messages like `tajnopis`.

### Kasiski Method

1. **Find repeated substrings** (e.g., 3+ characters).
2. **Measure distances** between repetitions.
3. **Compute GCDs** of distances.
4. Most frequent GCD = likely key length.

> Example output:
> `Suggested key lengths: [(113, 45352), (2, 22782), ...]`

### Frequency Analysis

Once key length is known:
1. Split ciphertext into `key_length` segments.
2. For each segment:
   - Analyze most frequent character.
   - Assume common plaintext character (e.g., space) and deduce key byte.
3. Reconstruct full key and decrypt.

---

### Usage

#### 1. Find Key Length

```bash
python KeyLengths.py
```

- Outputs a list of possible key lengths and their frequencies.

#### 2. Decrypt Ciphertext

- Edit `DecryptText.py` and set the correct `key_length` (e.g., `113`).
- Then run:

```bash
python DecryptText.py
```

- Output:
  - Key will be displayed.
  - Decrypted text saved to `decrypted_cipher.txt`.

---

## ✅ Results

- **Encryption**: Verified correct encryption/decryption of text (e.g., "David Blazheski Projekt pri predmetu IK.!").
- **Binary Decryption**: Successfully decrypted `šifrirana.png.vig` using `kljuc.vig`.
- **Cryptanalysis**: Cracked `tajnopis` (key length = 113) and recovered full text of *"Med dvema stoloma"* by Josip Jurčič.

---

## 📚 References

1. [Wikipedia – Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Friedman_test)
2. [Five Ways to Crack a Vigenère Cipher (Cipher Challenge)](https://www.cipherchallenge.org/wp-content/uploads/2020/12/Five-ways-to-crack-a-Vigenere-cipher.pdf)

---
