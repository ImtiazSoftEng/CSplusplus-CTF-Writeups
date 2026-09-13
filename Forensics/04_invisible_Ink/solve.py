with open("note.txt", "r", encoding="utf-8") as f:
    text = f.read()

bits = ""

for char in text:
    if ord(char) == 0x200B:
        bits += "0"
    elif ord(char) == 0x200C:
        bits += "1"

print("Number of hidden bits:", len(bits))

decoded = ""

for i in range(0, len(bits), 8):
    byte = bits[i:i+8]

    if len(byte) == 8:
        decoded += chr(int(byte, 2))

print("Decoded message:")
print(decoded)