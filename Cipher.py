def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = input("Enter message: ")
shift = int(input("Shift value: "))

choice = input("Encrypt (E) or Decrypt (D)? ").upper()

if choice == "E":
    print("Encrypted:", encrypt(msg, shift))
else:
    print("Decrypted:", decrypt(msg, shift))
