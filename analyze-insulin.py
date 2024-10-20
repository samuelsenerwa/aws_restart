with open('preproinsulin-seq-clean.txt', 'r') as file:
    lines = file.readlines()
    
cleaned_sequence = ''

for line in lines:
    if 'ORIGIN' in line or '//' in line:
        continue
    cleaned_sequence += line[10:].strip()
    
print(cleaned_sequence)

with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(cleaned_sequence)

preproinsulin_sequence = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaedlqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"

# Extract the parts of the sequence
insulin_seq = preproinsulin_sequence[:24]
lsinsulin_seq = preproinsulin_sequence[:24]  # Amino acids 1-24
binsulin_seq = preproinsulin_sequence[24:54]  # Amino acids 25-54
cinsulin_seq = preproinsulin_sequence[54:89]  # Amino acids 55-89
ainsulin_seq = preproinsulin_sequence[89:]  # Amino acids 90-110

# saving the sequence in their respective files
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin_seq)

with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin_seq)

with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin_seq)

with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin_seq)
