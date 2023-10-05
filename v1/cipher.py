import pycipher

def cipher(text, key):
    return pycipher.Caesar(key).encipher(text, keep_punct=True)