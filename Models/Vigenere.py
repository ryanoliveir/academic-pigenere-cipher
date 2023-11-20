
class Vigenere:
    def __init__(self):
        self._phrase = ""
        self._key  = ""



    @property
    def phrase(self):
        return self._phrase
    
    @phrase.setter
    def phrase(self, phrase):
        self._phrase = phrase


    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, key):
        if not self.isValidKey(key):
            
            key_chars = [char for char in key]
            
            while not self.isValidKey(key_chars):
                key_chars.append(key_chars[len(key_chars) % len(key)])
                print(key_chars)

            self._key = ''.join(key_chars)
        

    def isValidKey(self, key):
        if len(key) < len(self._phrase):
            return False
        return True
