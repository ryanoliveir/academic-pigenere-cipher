from art import *
from Models.Vigenere import Vigenere
import os
import sys

if __name__ == "__main__":

    os.system("cls || clear")

    vigenere_cypher = Vigenere()



    tprint("VIGENERE CYPHER")
    print("by Ryan Soares")

    args = sys.argv

    if len(sys.argv) > 3  and sys.argv[3] == "-v":
        verboseMode = True
    else:
        verboseMode = False


    if args[2] == "e":
        print("[*] Encrypt mode")
        phrase = input("[?] Provide the phrase: ")
        key = input("[?] Provide the key: ")


        vigenere_cypher.phrase = phrase
        vigenere_cypher.key = key

        print(f"[+] {vigenere_cypher.encrypt(verboseMode)}")

    elif args[2] == "d":
        print("[*] Decrypt mode")
        phrase = input("[?] Provide the encrypted phrase: ")
        key = input("[?] Provide the key: ")


        vigenere_cypher.phrase = phrase
        vigenere_cypher.key = key


        print(f"[+] {vigenere_cypher.decrypt(verboseMode)}")

    else:
        print("[!] Invalid --mode argument (use 'e' or 'd)")


