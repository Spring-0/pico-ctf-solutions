
def chall_1_func():
	return (79 << 7) // 3

def get_flag(target_arg):
	return "picoCTF{" + f"{target_arg:08x}" + "}"

target_arg = chall_1_func()

print(f"Argument required to win: {target_arg}")
print(f"Flag: {get_flag(target_arg)}")
