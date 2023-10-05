import pycipher

def cipher(text, key, _type):
    try:
        match _type:
            case 'Ceaser':
                key = int(key)
                cipher = pycipher.Caesar(key)
                result = cipher.encipher(text, keep_punct=True)
                return result
            case 'Railfence':
                key = int(key)
                cipher = pycipher.Railfence(key)
                result = cipher.encipher(text, keep_punct=True)
                return result
    except ValueError as e:
        print(f'Error: {e}')
        pass

def decipher(text, key, _type):
    try:
        match _type:
            case 'Ceaser':
                key = int(key)
                cipher = pycipher.Caesar(key)
                result = cipher.decipher(text, keep_punct=True)
                return result
            case 'Railfence':
                key = int(key)
                cipher = pycipher.Railfence(key)
                result = cipher.decipher(text, keep_punct=True)
                return result
    except ValueError as e:
        print(f'Error: {e}')
        pass