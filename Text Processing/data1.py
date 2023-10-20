import re

# Sample text
text = "Thyroid is an important gland in the body. Thyroid problems can cause various health issues. The Thyroid gland produces hormones."

# Find words containing "thyroid" or "Thyroid" in the text
searched_words = re.findall(r'\b(?:thyroid|Thyroid)\b', text)

# Display the results
if searched_words:
    print("Words containing 'thyroid' or 'Thyroid' found:")
    for word in searched_words:
        print(word)
else:
    print("No words containing 'thyroid' or 'Thyroid' found in the text.")
