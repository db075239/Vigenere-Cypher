from collections import Counter
def write_to_file(file_name, content, encoding='utf-8'):
    with open(file_name, 'w', encoding=encoding) as file:
        file.write(content)
def read_file(file):
    with open(file, 'rb') as file:
        return file.read()
def decrypt(data, key):
    decrypted = bytearray()
    for i, byte in enumerate(data):
        decrypted.append((byte - key[i % len(key)]) % 256)
    return decrypted.decode('utf-8')
def find_key(data, key_length):
    common_char = ord(' ')  
    parts = [data[i::key_length] for i in range(key_length)]
    key = bytearray()
    for segment in parts:
        most_common_byte = Counter(segment).most_common(1)[0][0]
        key_byte = (most_common_byte - common_char) % 256
        key.append(key_byte)
    return key
def break_vigenere(file, key_length):
    encrypted_data = read_file(file)  
    key = find_key(encrypted_data, key_length)  
    decrypted_text = decrypt(encrypted_data, key)  
    write_to_file("decrypted_cipher.txt", decrypted_text)
    print("Vaše besedilo je v datoteki decrypted_cipher.txt")
    return decrypted_text
file = "tajnopis"
key_length = 113
decrypted_text = break_vigenere(file, key_length)
