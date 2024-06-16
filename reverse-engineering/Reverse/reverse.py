local_38 = "7b4654436f636970";
local_30 = "337633725f666c33";
local_28 = "75735f676e693572";
local_20 = "6c75663535656363";
local_18 = "346434316237645f";

pass_parts = [local_38, local_30, local_28, local_20, local_18]

def to_ascii(hex_val):
    return bytes.fromhex(hex_val).decode("ascii")

password = "".join([to_ascii(hex_val)[::-1] for hex_val in pass_parts])
print(f"[+] password: {password}")
