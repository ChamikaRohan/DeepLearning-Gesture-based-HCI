def specific_words_finder(input_string, specific_words):
    for word in specific_words:
        if word in input_string:
            return True
    return False

"""
input_string = "I am using Microsoft center Word to write this document."
specific_words = ["Center"]

print(specific_words_finder(input_string, specific_words))  # Output: True

input_string = "I am using Notepad to write this document."
print(specific_words_finder(input_string, specific_words))  # Output: False
"""



