import sys
import os
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def main(argv):
    if(argv[1].lower() == "setup"):
        if len(argv) != 3:
            print("Wrong number of arguments for operation: " + argv[1])
            return False
        
        key = os.urandom(32)
        
        with open(argv[2], "wb") as key_file:
            key_file.write(key)
            
        print("Key saved to file: " + key.hex()[:16] + "... (truncated to first 16 characters)")
        
        return True
    elif(argv[1].lower() == "enc"):
        if len(argv) != 4:
            print("Wrong number of arguments for operation: " + argv[1])
            return False
        
        nonce = os.urandom(16)
        
        with open(argv[2], "rb") as file, open(argv[3], "rb") as key_file:
            key = key_file.read(32)
            algorithm = algorithms.ChaCha20(key, nonce)
            cipher = Cipher(algorithm, mode=None)
            encryptor = cipher.encryptor()
            cipher_text = encryptor.update(file.read())
            
            with open(argv[2] + ".enc", "wb") as enc_file:
                enc_file.write(nonce)
                enc_file.write(cipher_text)
                
            print("Cipher text successfully saved to file: " + argv[2] + ".enc with contents: " + cipher_text.hex()[:16] + "... (trucated to first 16 characters)")
        
        return True
    elif(argv[1].lower() == "dec"):
        if len(argv) != 4:
            print("Invalid number of arguments for operation: " + argv[1])
            return False
        
        with open(argv[2], "rb") as cipher_text_file:
            dec_nonce = cipher_text_file.read(16)
            print("Nonce has size: " + str(len(dec_nonce)) + " with contents: " + dec_nonce.hex())
            cipher_text = cipher_text_file.read()
            print("Cipher text has length: " + str(len(cipher_text)) + " with contents: " + cipher_text.hex())
            
        with open(argv[3], "rb") as key_file:
            key = key_file.read(32)
            
        algorithm = algorithms.ChaCha20(key, dec_nonce)
        cipher = Cipher(algorithm, mode=None)
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(cipher_text)
        
        with open(argv[2] + ".dec", "wb") as dec_file:
            dec_file.write(plaintext)
            
        print("Plain text successfully saved to file: " + argv[2] + ".dec with contents: " + plaintext.hex()[:16] + "... (truncated to first 16 characters)")
        
        return True
    else:
        print("Invalid operation: " + argv[1])
        return False    
    

if __name__ == "__main__":
    argv = sys.argv;
    if(len(argv) < 3 or len(argv) > 4):
        print("Invalid number of arguments!")
        
    else:
        if main(argv):
            print("\n\nProgram has run it's course!\n")
        else:
            print("\n\nProgram was not successful!\n")