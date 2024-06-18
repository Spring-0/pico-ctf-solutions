# rb-0x4 -> 0x9fe1a (654,874)

# if rbp-0x4 <= 0x2710 (10,000):
# 	jump to +37
# 	rb-0x4 = rb-0x4 + 0x65 (101)
# 	eax = rb-0x4
# else
# 	rbp-0x4 = rbp-0x4 - 0x65 (101)
#	eax = rbp-0x4
#

eax = 654874 - 101
print("picoCTF{" + str(eax) + "}")