# rbp-0xc -> 0x9fe1a
# eax = 0x9fe1a * 0x4
# eax = eax + 0x1f5


eax = int("0x9fe1a", 16) * int("0x4", 16) + int("0x1f5", 16)
print("picoCTF{" + str(eax) + "}")

