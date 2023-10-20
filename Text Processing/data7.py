import re

# Sample text
text = "Renal function is essential for maintaining electrolytes balance. Renal disorders can affect electrolytes levels. The patient's Electrolytes were measured."

# Find words containing "renal" or "Renal"
renal_pattern = r'\b(?:renal|Renal)\b'

# Find words containing "electrolytes" or "Electrolytes"
electrolytes_pattern = r'\b(?:electrolytes|Electrolytes)\b'

# Find and display the results
renal_matches = re.findall(renal_pattern, text)
electrolytes_matches = re.findall(electrolytes_pattern, text)

if renal_matches:
    print("Words containing 'renal' or 'Renal':")
    for word in renal_matches:
        print(word)

if electrolytes_matches:
    print("Words containing 'electrolytes' or 'Electrolytes':")
    for word in electrolytes_matches:
        print(word)
