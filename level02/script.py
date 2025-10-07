s = '0x756e505234376848 0x45414a3561733951 0x377a7143574e6758 0x354a35686e475873 0x48336750664b394d'

# Split the string by spaces into separate hex values
hex_values = s.split()
decoded=""
# Convert each "0x..." hex string into bytes, then decode as ASCII
for h in hex_values:
    decoded += ''.join(bytes.fromhex(h[2:]).decode('utf-8')[::-1])
    

# Reverse the entire message (if needed)
print(decoded)
