from Models.Alphabet import Alphabet

class Vigenere:
    def __init__(self):
        self._phrase = ""
        self._key  = ""



    @property
    def phrase(self):
        return self._phrase
    
    @phrase.setter
    def phrase(self, phrase):
        phrase = phrase.upper()
        self._phrase = phrase.replace(" ", "")


    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, key):
        key = key.upper()
        if not self.isValidKey(key):
            
            key_chars = [char for char in key]
            
            while not self.isValidKey(key_chars):
                key_chars.append(key_chars[len(key_chars) % len(key)])
            self._key = ''.join(key_chars)
        

    def isValidKey(self, key):
        if len(key) < len(self._phrase):
            return False
        return True



    def encrypt(self, verbose_mode):

        alphabet = Alphabet()
        alphabet.init()

        print("[+] Encrypting message...")

        phrase_values = []
        key_values = []

        sizeOfMessage = len(self._phrase)
        for index in range(sizeOfMessage):
            for latter_phrase in alphabet.alphabet:
                if (self._phrase[index] == latter_phrase.latter ):
                    phrase_values.append(latter_phrase.number)
                    


        for index in range(sizeOfMessage):
            for latter_key in alphabet.alphabet:
                if (self._key[index] == latter_key.latter):
                    key_values.append(latter_key.number)

      


        encrypt_values = []
        for index in range(sizeOfMessage):
            if phrase_values[index] + key_values[index] > 5:
                encrypt_values.append((phrase_values[index] + key_values[index]) % 26)
            else:
                encrypt_values.append(phrase_values[index] + key_values[index])

        


        encrypted_phrase = ""

        for encryptLatterNumber in encrypt_values:
            for latter in alphabet.alphabet:
                if encryptLatterNumber == latter.number:
                    encrypted_phrase += latter.latter
            

        if verbose_mode:
            print(phrase_values)
            print(key_values)
            print(encrypt_values)

        return encrypted_phrase.lower()



    def decrypt(self, verbose_mode):

        alphabet = Alphabet()
        alphabet.init()

        print("[+] Encrypting message...")

        phrase_values = []
        key_values = []

        sizeOfMessage = len(self._phrase)
        for index in range(sizeOfMessage):
            for latter_phrase in alphabet.alphabet:
                if (self._phrase[index] == latter_phrase.latter ):
                    phrase_values.append(latter_phrase.number)
                    


        for index in range(sizeOfMessage):
            for latter_key in alphabet.alphabet:
                if (self._key[index] == latter_key.latter):
                    key_values.append(latter_key.number)


        encrypt_values = []
        for index in range(sizeOfMessage):
            if phrase_values[index] - key_values[index] < 0:
                encrypt_values.append((phrase_values[index] - key_values[index]) + 26)
            else:
                encrypt_values.append(phrase_values[index] - key_values[index])



        decrypt_phrase = ""

        for encryptLatterNumber in encrypt_values:
            for latter in alphabet.alphabet:
                if encryptLatterNumber == latter.number:
                    decrypt_phrase += latter.latter
        
        
        if verbose_mode:
            print(phrase_values)
            print(key_values)
            print(encrypt_values)

        return decrypt_phrase.lower()
