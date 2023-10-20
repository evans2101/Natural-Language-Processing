import re

# Sample text
text = "The patient had a . recurrent. infection. Bilirubin levels were monitored for liver function. The .recurrent condition is concerning."

# Find words enclosed by periods (".") on both sides
enclosed_by_periods_pattern = r'\.\s(\w+)\s\.'

# Find words containing "bilirubin" or "Bilirubin"
bilirubin_pattern = r'\b(?:bilirubin|Bilirubin)\b'

# Find and display the results
enclosed_by_periods_matches = re.findall(enclosed_by_periods_pattern, text)
bilirubin_matches = re.findall(bilirubin_pattern, text)

if enclosed_by_periods_matches:
    print("Words enclosed by periods (\".\") on both sides:")
    for word in enclosed_by_periods_matches:
        print(word)

if bilirubin_matches:
    print("Words containing 'bilirubin' or 'Bilirubin':")
    for word in bilirubin_matches:
        print(word)
