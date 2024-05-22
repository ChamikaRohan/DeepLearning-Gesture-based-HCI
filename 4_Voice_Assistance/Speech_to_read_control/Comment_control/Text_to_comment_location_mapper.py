import sys
from Comment_creater import comment_creater

sys.path.append('../4_Voice_Assistance/Speech_to_application')
from Words_finder import specific_words_finder

def text_to_comment_location_mapper(input_string):
    location_dict = ["top left", "top right", "bottom left", "bottom right", "center", "middle"]
    input_string_lower = input_string.lower()
    if specific_words_finder(input_string_lower, [location_dict[0]]):
        comment_creater(location_dict[0])
    elif specific_words_finder(input_string_lower, [location_dict[1]]):
        comment_creater(location_dict[1])
    elif specific_words_finder(input_string_lower, [location_dict[2]]):
        comment_creater(location_dict[2])
    elif specific_words_finder(input_string_lower, [location_dict[3]]):
        comment_creater(location_dict[3])
    elif ( specific_words_finder(input_string_lower, [location_dict[4]]) or specific_words_finder(input_string_lower, [location_dict[5]])):
        comment_creater(location_dict[4])
    else:
        return


