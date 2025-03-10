import sys

def main(key_len, cyphertext, match_words):
    c_key_len = int(key_len)
    c_cyphertext = cyphertext.upper()
    c_matches = [match.upper() for match in match_words]
    
    read = 0
    while True:
        if read >= len(c_cyphertext):
            break
        
        slice = ""
        if read + c_key_len >= len(c_cyphertext):
            slice = c_cyphertext[read:]
        else:
            slice = c_cyphertext[read:read+c_key_len]
        
        print(slice)
        read += c_key_len
    return

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Wrong number of arguments!")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3:])