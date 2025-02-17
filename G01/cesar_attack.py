import sys
import cesar

def main(text, matches):
    curated_matches = []
    for keyword in matches:
        curated_matches.append(keyword.upper())
    for key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        decoded = cesar.main("dec", key, text, False)
        for keyword in curated_matches:
            if keyword in decoded:
                print("Key: " + key)
                print("Decoded text: " + decoded)
                return
    print("Couldn't decode!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Too few arguments!")
    else:
        main(sys.argv[1], sys.argv[2:])