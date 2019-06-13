# Collection of input and outputs

YES_IN = ['yes', 'ya', 'yea', 'ok', 'sure', 'fine', 'yeah']

CHAT_WORDS = ['chat', 'talk', 'converse', 'hang', 'speak']

HAPPY_WORDS = ['happy', 'jovial', 'glad', 'good']
SAD_WORDS = ['sad', 'upset', 'unhappy', 'blue', 'simpy']
SCARED_WORDS = ['scared', 'terrified', 'spooked', 'nervous']
EXCITED_WORDS = ['excited', 'ecstatic', 'hyper', 'pumped']
AMUSED_WORDS = ['amused', 'lol', 'okay', 'ok', 'cool']
LOVED_WORDS = ['loved', 'emotional', 'love', 'appreciated']
LUCKY_WORDS = ['lucky', 'spontaneous', 'bored']

MOOD_MAP = {'happy': HAPPY_WORDS, 'sad': SAD_WORDS, 'scared': SCARED_WORDS, 
               'amused': AMUSED_WORDS, 'loved': LOVED_WORDS, 'lucky': LUCKY_WORDS}

POS_IN = HAPPY_WORDS + EXCITED_WORDS + AMUSED_WORDS + LOVED_WORDS + LUCKY_WORDS
POS_OUT = ['yay!', 'that\'s good!', 'keep it up!', 'great!']

NEG_IN = SAD_WORDS + SCARED_WORDS 
NEG_OUT = ['it\'s going to be ok', 'i\'m here for you', 'you got this!', 'i\'m sorry']

RANDOM_OUT = ['cool', 'ok', 'interesting']