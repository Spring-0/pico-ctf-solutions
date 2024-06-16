# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ

# 38 Total plain text characters
# 19 Encoded characters
# Each encoded character is 2 plain characters

encoded = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"


# def encode_char_pair(char1, char2):
# 	encoded_char = chr((ord(char1) << 8) + ord(char2))
# 	print(encoded_char)

def decode_string(encoded_string):
	decoded = []
	for ch in encoded_string:
		val = ord(ch)
		ch1 = chr(val >> 8)
		ch2 = chr(val & 0xFF)
		decoded.append(ch1)
		decoded.append(ch2)
	print(decoded)
	return "".join(decoded)


decoded_str = decode_string(encoded)
print(decoded_str)


