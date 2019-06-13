import moodipy.functions as moodipy
import copy
from moodipy.songs import *

def test_all():
    test_pick_song()
    test_add_song()
    test_check_in_map_lists()
    test_input_with_msg()

def test_pick_song():
    assert moodipy.pick_song('happy') in [BETTER_NOT, PARADISE, BUBBLY]
    assert moodipy.pick_song('sad') in [HIGH_HOPES, DANCING_STRANGER, SAY_SOMETHING]
    assert moodipy.pick_song('scared') in [LANDSLIDE, SPARROWS, WONT_GIVE_UP]
    assert moodipy.pick_song('excited') in [FOUND_LOVE, BROCCOLI, HUMBLE]
    assert moodipy.pick_song('amused') in [FLAMINGO, FOX, COCONUT]
    assert moodipy.pick_song('loved') in [WAY_YOU_ARE, BEST_PART, EVERY_WAY]
    assert moodipy.pick_song('lucky') in SONG_LIST

def test_add_song():
    songs_backup = copy.deepcopy(moodipy.songs)
    moodipy.add_song('funky', 'test_url')
    assert moodipy.pick_song('funky') == 'test_url'
    # Reset the songs so that our test_url does not interfere with other tests.
    moodipy.songs = copy.deepcopy(songs_backup)
    
def test_check_in_map_lists():
    test_map = {1: ['a', 'b'], 2: ['c', 'd']}
    assert moodipy.check_in_map_lists(['b'], test_map) == 1
    assert moodipy.check_in_map_lists(['e'], test_map) == ''

def test_input_with_msg():
    # Generally, input_with_msg will take input from the user, but we just add an argument to simulate user input.
    assert moodipy.input_with_msg(question='Question?', user_input='This is a string.') == ['this', 'is', 'a', 'string']

### Following test functions are copied from assignment A3 - Chatbots
def test_remove_punctuation():
    assert callable(moodipy.remove_punctuation)
    assert isinstance(moodipy.remove_punctuation('a'), str)
    assert moodipy.remove_punctuation("Hey! It's Professor Ellis!") == "Hey Its Professor Ellis"

def test_prepare_text():
    assert callable(moodipy.prepare_text)
    assert isinstance(moodipy.prepare_text('One two three.'), list)
    assert moodipy.prepare_text('Hi! Also, howdy.') == ['hi', 'also', 'howdy']
    
def test_selector():
    assert callable(moodipy.selector)
    assert moodipy.selector(['in', 'words'], ['words'], ['yes']) == 'yes'
    assert moodipy.selector(['in', 'words'], ['out'], ['yes']) == None

def test_end_chat():
    assert callable(moodipy.end_chat)
    assert isinstance(moodipy.end_chat(['a', 'b']), bool)
    assert moodipy.end_chat(['quit']) == True