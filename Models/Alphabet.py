from Models.Latter import Latter

import string
class Alphabet:
    def __init__(self):
        self.alphabet = []
        self.latters = list(string.ascii_uppercase)


    def init(self):
        for index, latter in enumerate(self.latters):
            latter = Latter(latter, index)
            self.alphabet.append(latter)



