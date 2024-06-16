"""
Key length must match key_full_template_trial (32 chars)

key_part_static1_trial + u_trial_dig[4] + u_trial_dig[5] + u_trial_dig[3]
	+ u_trial_dig[6] + u_trial_dig[2] + u_trial_dig[7] + u_trial_dig[1] + u_trial_dig[8] + }
"""

import hashlib

bUsername_trial = b"GOUGH"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

index_sequence = [4, 5, 3, 6, 2, 7, 1, 8]
u_trial_dig = hashlib.sha256(bUsername_trial).hexdigest()

key = key_part_static1_trial + "".join([u_trial_dig[i] for i in index_sequence]) + "}"

print(f"[+] Key generated: {key}")

