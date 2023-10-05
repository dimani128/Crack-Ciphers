
# Adapted from https://www.scaler.com/topics/caesar-cipher-python/

class Ceaser:
    def __init__(self):
        pass

    def encipher(self, text, key):
        ans = ""
        # iterate over the given text
        for i in range(len(text)):
            ch = text[i]
            
            # check if space is there then simply add space
            if ch==" ":
                ans+=" "
            # check if a character is uppercase then encrypt it accordingly 
            elif (ch.isupper()):
                ans += chr((ord(ch) + key-65) % 26 + 65)
            # check if a character is lowercase then encrypt it accordingly
            
            else:
                ans += chr((ord(ch) + key-97) % 26 + 97)
    
        return ans

    def decipher(self, text, key):
        return self.encipher(text, -key)