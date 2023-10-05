
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from ciphering import ceaser, railfence, affine

def cipher(text, key, key2, _type):
    try:
        match _type:
            case 'Ceaser':
                key = int(key)
                cipher = ceaser.Ceaser()
                result = cipher.encipher(text, key)
                return result
            case 'Railfence':
                key = int(key)
                cipher = railfence.Railfence()
                result = cipher.encipher(text, key)
                return result
            case 'Affine':
                key = int(key)
                key2 = int(key2)
                cipher = affine.Affine()
                result = cipher.encipher(text, key, key2)
                return result
    except ValueError as e:
        if 'invalid literal for int() with base 10' in str(e):
            print(f'Error: {e}')
        else:
            raise e
        pass

def decipher(text, key, key2, _type):
    try:
        match _type:
            case 'Ceaser':
                key = int(key)
                cipher = ceaser.Ceaser()
                result = cipher.decipher(text, key)
                return result
            case 'Railfence':
                key = int(key)
                cipher = railfence.Railfence()
                result = cipher.decipher(text, key)
                return result
            case 'Affine':
                key = int(key)
                key2 = int(key2)
                if type(key) != int or type(key2) != int:
                    print(type(key), type(key2))
                cipher = affine.Affine()
                result = cipher.decipher(text, key, key2)
                # try:
                #     result = cipher.decipher(text, key, key2)
                # except TypeError as e:
                #     print(f'Error: {e}, key: {key}, key2: {key2}, text: {text}.')
                #     return
                return result
    except (ValueError, ZeroDivisionError) as e:
        if 'invalid literal for int() with base 10' in str(e):
            print(f'Error: {e}')
        else:
            raise e
        pass