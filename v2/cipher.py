import pycipher

def cipher(text, key, _type):
    match _type:
        case 'Ceaser':
            try:
                key = int(key)
                cipher = pycipher.Caesar(key)
                result = cipher.encipher(text, keep_punct=True)
                return result
            except ValueError:
                pass

def decipher(text, key, _type):
    match _type:
        case 'Ceaser':
            try:
                key = int(key)
                cipher = pycipher.Caesar(key)
                result = cipher.decipher(text, keep_punct=True)
                return result
            except ValueError:
                pass
        case 'Ceaser':
            try:
                key = int(key)
                cipher = pycipher.Caesar(key)
                result = cipher.decipher(text, keep_punct=True)
                return result
            except ValueError:
                pass