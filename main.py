from art import *
from Models.Alphabet import Alphabet
from Models.Vigenere import Vigenere
import os

if __name__ == "__main__":

    os.system("cls || clear")


    alphabet = Alphabet()
    alphabet.init()

    vigenere_cypher = Vigenere()



    tprint("VIGENERE CYPHER")
    print("by Ryan Soares")


    phrase = input("[?] Provide the phrase: ")
    key = input("[?] Provide the key: ")


    vigenere_cypher.phrase = phrase
    vigenere_cypher.key = key


    print(vigenere_cypher.phrase)
    print(vigenere_cypher.key)





