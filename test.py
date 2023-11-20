import unittest
from Models.Vigenere import Vigenere  # Replace 'your_module' with the actual module name

class TestVigenereCipher(unittest.TestCase):
    def test_encryption_lower_case(self):
        vigenere_cypher = Vigenere()
        vigenere_cypher.phrase = "helloworld"
        vigenere_cypher.key = "key"

        encrypted_text = vigenere_cypher.encrypt()
        self.assertEqual(encrypted_text, "rijvsuyvjn")

    def test_decryption_lower_case(self):
        vigenere_cypher = Vigenere()
        vigenere_cypher.phrase = "rijvsuyvjn"
        vigenere_cypher.key = "key"

        decrypted_text = vigenere_cypher.decrypt()
        self.assertEqual(decrypted_text, "helloworld")


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()