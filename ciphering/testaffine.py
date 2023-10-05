
class AffineCipher:
    def __init__(self):
        pass

    def encipher(self, text, a, b):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    encrypted_char = chr(((ord(char) - ord('a')) * a + b) % 26 + ord('a'))
                else:
                    encrypted_char = chr(((ord(char) - ord('A')) * a + b) % 26 + ord('A'))
            else:
                encrypted_char = char
            encrypted_text += encrypted_char
        return encrypted_text

    def decipher(self, text, a, b):
        decrypted_text = ""
        a_inverse = self.modular_inverse(a, 26)
        
        for char in text:
            if char.isalpha():
                if char.islower():
                    decrypted_char = chr(((ord(char) - ord('a') - b) * a_inverse) % 26 + ord('a'))
                else:
                    decrypted_char = chr(((ord(char) - ord('A') - b) * a_inverse) % 26 + ord('A'))
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        return decrypted_text

    def modular_inverse(self, a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

# Example usage:
affine_cipher = AffineCipher()
text = "The quick brown fox jumps over 13 lazy dogs."
a = 5
b = 8
encrypted_text = affine_cipher.encipher(text, a, b)
decrypted_text = affine_cipher.decipher(encrypted_text, a, b)

print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
