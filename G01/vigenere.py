import sys

def main(operation, key, plaintext):
    c_key = key.upper()
    key_len = len(c_key)
    c_plaintext = plaintext.upper()
    text = ""
    i = 0
    while i < len(c_plaintext):
        key_val = ord(c_key[i % key_len]) - ord("A")
        plain_c = ord(c_plaintext[i]) - ord("A")
        if operation.upper() == "ENC":
            text += chr((plain_c + key_val) % 26 + ord("A"))
        elif operation.upper() == "DEC":
            text += chr((plain_c - key_val) % 26 + ord("A"))
        i += 1
    return text

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong number of arguments!")
    else:
        cypher = main(sys.argv[1], sys.argv[2], sys.argv[3])
        print(cypher)  