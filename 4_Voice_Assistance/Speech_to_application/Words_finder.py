def specific_words_finder(input_string, specific_words):
    for word in specific_words:
        if word in input_string:
            return True
    return False

"""
input_string = "I am using Microsoft Word to write this document."
specific_words = ["Microsoft Word", "Google Docs", "LibreOffice"]

print(contains_specific_words(input_string, specific_words))  # Output: True

input_string = "I am using Notepad to write this document."
print(contains_specific_words(input_string, specific_words))  # Output: False
"""

