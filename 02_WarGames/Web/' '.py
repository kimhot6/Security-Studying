hex_data = "e2 80 8e e2 80 8e e2 80 8e 44 e2 80 8e 48 7b 44 e2 80 8e 6f 5f e2 80 8e e2 80 8e 59 6f e2 80 8e 75 e2 80 8e 5f 42 65 e2 80 8e e2 80 8e 6c 69 e2 80 8e e2 80 8e 65 e2 80 8e 76 65 e2 80 8e 5f e2 80 8e 57 e2 80 8e 68 61 e2 80 8e 74 e2 80 8e 5f 79 e2 80 8e 6f e2 80 8e 75 e2 80 8e 5f 53 e2 80 8e 65 e2 80 8e 65 e2 80 8e 5f 6f e2 80 8e 6e e2 80 8e 5f 74 e2 80 8e 68 e2 80 8e 65 5f e2 80 8e 77 e2 80 8e 65 62 e2 80 8e 3f e2 80 8e 7d"

raw_bytes = bytes.fromhex(hex_data.replace(' ', ''))
clean_flag = "".join([chr(b) for b in raw_bytes if b < 128])

print(clean_flag)
