import pycipher

def cipher(text, key, key2, _type):
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
            case 'Affine':
                key = int(key)
                key = int(key2)
                cipher = pycipher.Affine(a=key, b=key2)
                result = cipher.encipher(text, keep_punct=True)
                return result
    except ValueError as e:
        print(f'Error: {e}')
        pass

def decipher(text, key, key2, _type):
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
            case 'Affine':
                key = int(key)
                key = int(key2)
                cipher = pycipher.Affine(key, key2)
                result = cipher.decipher(text, keep_punct=True)
                return result
    except (ValueError, ZeroDivisionError) as e:
        print(f'Error: {e}')
        pass