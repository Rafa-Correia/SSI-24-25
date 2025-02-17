import sys

def main(operation, key, plaintext, display = True):
    offset = ord(key.upper()) - 65
    curated_plaintext = plaintext.upper()
    cyphertext = ""
    if operation.lower() == "enc":
        for c in curated_plaintext:
            cyphertext += chr((ord(c) - 65 + offset) % 26 + 65)
        if display:
            print("Cypher: " + cyphertext)
        return cyphertext
    elif operation.lower() == "dec":
        for c in curated_plaintext:
            cyphertext += chr((ord(c) - 65 - offset) % 26 + 65)
        if display:
            print("Plaintext: " + cyphertext)
        return cyphertext
    else:
        print("Operation not supported.")
        return
            
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong number of arguments!")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])