import re

# Sample text
text = "The new employee has great potential. Potential candidates should apply. Hysterectomy is a surgical procedure. Hysterectomy may be necessary in some cases."

# Find words ending with "potential" or "Potential"
potential_pattern = r'\b\w+(?:potential|Potential)\b'

# Find words starting with "hysterectomy" or "Hysterectomy"
hysterectomy_pattern = r'\b(?:hysterectomy|Hysterectomy)\w+\b'

# Find and display the results
potential_matches = re.findall(potential_pattern, text, flags=re.IGNORECASE)
hysterectomy_matches = re.findall(hysterectomy_pattern, text)

if potential_matches:
    print("Words ending with 'potential' or 'Potential':")
    for word in potential_matches:
        print(word)

if hysterectomy_matches:
    print("Words starting with 'hysterectomy' or 'Hysterectomy':")
    for word in hysterectomy_matches:
        print(word)
