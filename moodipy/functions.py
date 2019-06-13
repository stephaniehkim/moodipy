"""A collection of function for doing my project."""

import random
import string
from moodipy.songs import *

#dictionary list of moods mapped to the songs 
songs = {
'happy': [BETTER_NOT, PARADISE, BUBBLY],
'sad': [HIGH_HOPES, DANCING_STRANGER, SAY_SOMETHING],
'scared': [LANDSLIDE, SPARROWS, WONT_GIVE_UP],
'excited': [FOUND_LOVE, BROCCOLI, HUMBLE],
'amused': [FLAMINGO, FOX, COCONUT],
'loved': [WAY_YOU_ARE, BEST_PART, EVERY_WAY]
}

def pick_song(mood):
    
    """
    Pick a song based on the user's current mood
    
    Parameters 
    ----------
    mood: str
        User's current mood 
        
    Returns 
    -------
    output: str
        Song based on the mood 
    """

    output = ''
    if mood in songs:
        output = random.choice(songs[mood])
    elif mood == 'lucky':
        random_mood = random.choice(list(songs.keys()))
        output = random.choice(songs[random_mood])
    return output

def add_song(mood, song):
    
    """
    User adds a song link based on their current mood
    
    Parameters
    ----------
    mood: str 
        User's current mood 
    song: str 
        Spotify link to a song of user's choice 
        
    """
    
    if mood in songs:
        songs[mood].append(song)
    else:
        songs[mood] = [song]

def check_in_map_lists(input_list, input_map):
    
    """
    Check if words in the list match a word in the map of lists. Returns the key of the list.
    
    Parameters 
    ----------
    input_list: str
        List of strings of the user's current mood 
    input_map: str 
        Map of lists of moods to be searched
        
    Returns 
    -------
    key: str
        User's mood 
    """
    
    for key in input_map:
        if is_in_list(input_list, input_map[key]):
            return key
    return ''
    
def input_with_msg(question, clarification_q = 'Please put a response :(', user_input=''):
    
    """
    Request and sanitize a input from the user, by asking question. 
    Ask clarification_q if the user puts an empty string.
    
    Parameters
    ----------
    question: str
        Question request asked to the user 
    clarification_q: str
        Asking for clarification if an empty string is returned 
    user_input: str
        User's input to the question 
        
    Returns
    -------
    user_input: str 
        User's input to the question
    """
    
    while user_input == '':
        user_input = input(str(question) + '\t')
        user_input = prepare_text(user_input)
        if len(user_input) == 0:
            print(clarification_q)
            user_input = ''
        else:
            return user_input
    return prepare_text(user_input)
        
### Following functions are copied from assignment A3 - Chatbots
def remove_punctuation(input_string): 
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
    return out_string

def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list 

def selector(input_list, check_list, return_list):
    output = None
    for element in input_list: 
        if element in check_list:
            output = random.choice(return_list)
            break 
    return output 

def end_chat(input_list):
    if 'quit' in input_list:
        output = True
    else: 
        output = False 
    return output 

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False