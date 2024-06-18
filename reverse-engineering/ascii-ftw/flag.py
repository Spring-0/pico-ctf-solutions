
# Retrieved from ghidra
flag_raw = [
    "0x70",
    "0x69",
    "0x63",
    "0x6f",
    "0x43",
    "0x54",
    "0x46",
    "0x7b",
    "0x41",
    "0x53",
    "0x43",
    "0x49",
    "0x49",
    "0x5f",
    "0x49",
    "0x53",
    "0x5f",
    "0x45",
    "0x41",
    "0x53",
    "0x59",
    "0x5f",
    "0x38",
    "0x39",
    "0x36",
    "0x30",
    "0x46",
    "0x30",
    "0x41",
    "0x46",
    "0x7d"
]

flag = "".join(chr(int(flag_char, 16)) for flag_char in flag_raw)
print(f"[+] Flag: {flag}")