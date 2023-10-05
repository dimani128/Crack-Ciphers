
class Affine:
    def __init__(self):
        pass

    def encipher(self, text, a, b):
        print(text, a, b)
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
        raise ValueError(f'No inverse for {a} found.')
        return None