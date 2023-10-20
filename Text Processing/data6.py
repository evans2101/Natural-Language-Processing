import re

# Sample text
text = "The patient is at stage III of the disease. Stage iii is a critical condition. The candidate must have sufficient English skills. Sufficient English proficiency is required."

# Find words starting with "stage iii" or "Stage III"
stage_pattern = r'\b(?:stage\s+iii|Stage\s+III)\b'

# Find words containing "sufficient english" or "Sufficient English"
sufficient_english_pattern = r'\b(?:sufficient\s+english|Sufficient\s+English)\b'

# Find and display the results
stage_matches = re.findall(stage_pattern, text)
sufficient_english_matches = re.findall(sufficient_english_pattern, text)

if stage_matches:
    print("Words starting with 'stage iii' or 'Stage III':")
    for word in stage_matches:
        print(word)

if sufficient_english_matches:
    print("Words containing 'sufficient English' or 'Sufficient English':")
    for word in sufficient_english_matches:
        print(word)
