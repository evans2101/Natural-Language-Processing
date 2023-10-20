import re

# Sample text
text = "The patient received a confirmed diagnosis. A Confirmed Diagnosis was given to the patient. The doctor provided a confirmed diagnosis."

# Find words starting with "confirmed diagnosis" or "Confirmed Diagnosis"
confirmed_diagnosis_pattern = r'\b(?:confirmed\s+diagnosis|Confirmed\s+Diagnosis)\w*\b'

# Find and display the results
confirmed_diagnosis_matches = re.findall(confirmed_diagnosis_pattern, text)

if confirmed_diagnosis_matches:
    print("Words starting with 'confirmed diagnosis' or 'Confirmed Diagnosis':")
    for word in confirmed_diagnosis_matches:
        print(word)
