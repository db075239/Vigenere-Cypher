from getpass4 import getpass
import sys
def read_binary_file(filepath):
    """Prebere vsebino binarne datoteke in jo vrne kot bajtno zaporedje."""
    with open(filepath, "rb") as file:
        return file.read()
def write_binary_file(filepath, data):
    """Zapiše bajtno zaporedje v binarno datoteko."""
    with open(filepath, "wb") as file:
        file.write(data)
def load_code_table(filename):
    """Naloži kodno tabelo iz datoteke in obravnava posebne primere."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        code_table = {}
        for line in file:
            parts = line.split()
            key = parts[1]
            value = int(parts[0])
            if key == "<presledek>":
                key = " "
            code_table[key] = value       
        return code_table
def vigenere(data, key, mode='encrypt', code_table=None):
    """
    Univerzalna funkcija za šifriranje ali dešifriranje.
    Če je podana kodna tabela, jo uporabi za šifriranje/dešifriranje besedila.
    """
    key_length = len(key)
    if key_length == 0:
        raise ValueError("Napaka: Ključ ne sme biti prazen.")
    result = []
    if code_table:
        reverse_table = {v: k for k, v in code_table.items()}  # Obrnjena tabela za iskanje znakov
        for i, char in enumerate(data):
            if char in code_table:
                char_code = code_table[char]
                key_code = code_table[key[i % key_length]]
                shift = char_code + key_code if mode == 'encrypt' else char_code - key_code
                result.append(reverse_table[shift % len(code_table)])
            else:
                result.append(char)  # Nepoznane znake ohranimo
        return ''.join(result)
    else:
        # Za binarne podatke
        return bytes((byte + key[i % key_length]) % 256 if mode == 'encrypt' 
                     else (byte - key[i % key_length]) % 256 for i, byte in enumerate(data))
def main():
    print("Vigenere cipher za besedila in poljubne datoteke")
    choice = input("Vnesite 1 za šifriranje/desifriranje besedila ali 2 za šifriranje/desifriranje datoteke:").strip()
    if choice == '1':  # Šifriranje/dešifriranje besedila
        code_table = load_code_table("Vaja2bTabela.txt")
        plaintext = input("Vnesite besedilo za šifriranje: ")
        key = getpass("Vnesite ključ: ")
        # Šifriranje
        encrypted_text = vigenere(plaintext, key, mode='encrypt', code_table=code_table)
        print(f"Šifrirano besedilo: {encrypted_text}")
        # Dešifriranje
        decrypted_text = vigenere(encrypted_text, key, mode='decrypt', code_table=code_table)
        print(f"Dešifrirano besedilo: {decrypted_text}")
    elif choice == '2':  # Šifriranje/dešifriranje datotek
        input_file = input("Vnesite ime vhodne datoteke: ")
        key_input = input("Izbira ključa: 1) vnesi datoteko; 2) vnesi ključa preko tipkovnice: ").strip() #preko tipkovnice nisem poskusil ce dela
        mode = input("Vnesite način (encrypt ali decrypt): ").strip().lower()
        output_file = input("Vnesite ime izhodne datoteke: ")
        # Preberi vhodno datoteko
        data = read_binary_file(input_file)
        # Preberi ključ
        if key_input == '1':
            key_file = input("Vnesite ime datoteke s ključem: ")
            key = read_binary_file(key_file)
        elif key_input == '2':
            key = getpass("Vnesite ključ: ").encode('utf-8')
        # Izvedi šifriranje ali dešifriranje
        result = vigenere(data, key, mode)
       # Shrani rezultat v izhodno datoteko
        write_binary_file(output_file, result)
        print(f"Operacija '{mode}' je bila uspešno izvedena. Izhod je v datoteki '{output_file}'.")
if __name__ == "__main__":
    main()
