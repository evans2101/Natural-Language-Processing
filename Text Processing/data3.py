import re

# Sample text
text = "Lymphoma is a type of cancer. Lymphoma may be classified as grade III or grade II. The patient was diagnosed with Grade III lymphoma."

# Find words containing "lymphoma" or "Lymphoma"
lymphoma_pattern = r'\b(?:lymphoma|Lymphoma)\b'
lymphoma_matches = re.findall(lymphoma_pattern, text)

# Find words containing "grade iii" or "Grade III"
grade_pattern = r'\b(?:grade\s+iii|Grade\s+III)\b'
grade_matches = re.findall(grade_pattern, text)

# Display the results
if lymphoma_matches:
    print("Words containing 'lymphoma' or 'Lymphoma':")
    for word in lymphoma_matches:
        print(word)

if grade_matches:
    print("Words containing 'grade iii' or 'Grade III':")
    for word in grade_matches:
        print(word)
