import re

# Sample text
text = "The patient was diagnosed with stage IVB cancer. CNS disorders can be challenging to diagnose. She is at stage III. CNS disorders are serious."

# Find words starting with "stage" followed by letters
stage_pattern = r'\bstage\s+[a-zA-Z]+\b'
stage_matches = re.findall(stage_pattern, text, flags=re.I)  # flags=re.I for case-insensitive search

# Find words containing "cns" or "CNS"
cns_pattern = r'\b(?:cns|CNS)\b'
cns_matches = re.findall(cns_pattern, text)

# Display the results
if stage_matches:
    print("Words starting with 'stage' followed by letters:")
    for word in stage_matches:
        print(word)

if cns_matches:
    print("Words containing 'cns' or 'CNS':")
    for word in cns_matches:
        print(word)
