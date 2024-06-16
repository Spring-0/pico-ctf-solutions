import base64

encoded_key = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"
print("Flag: picoCTF{"
	+ base64.b64decode(encoded_key).decode('utf-8')
	+ "}")