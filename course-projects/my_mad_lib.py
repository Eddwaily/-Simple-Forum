from random import randint

parts_of_speech  = ["VERB,""PLACE", "PERSON", "PLURALNOUN", "NOUN"]

list_of_sentences= [
"This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here.",
"WOW...what a nice NOUN you have in there",
"Sometimes I VERB my self to death,Even PERSON knows that",
"let's go eat NOUN in PLACE, they've got a lot of PLURALNOUN in there",
"PERSON told that he bought a new NOUN that he met in PLACE, where they sell PLURALNOUN"]

length_of_list = len( list_of_sentences )
def word_in_pos( word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for thing in ml_string :
        if( word_in_pos( thing, parts_of_speech )==None ):
            replaced.append(thing)
        else:
            pos = word_in_pos( thing, parts_of_speech)
            prefix = thing[ 0 : thing.find(pos) ]
            pos_end_place = thing.find(pos) + len(pos)
            suffix = thing[ pos_end_place :  ]
            user_input = raw_input("Enter a "+pos)
            replaced.append( prefix + user_input + suffix )
    replaced = " ".join(replaced)
    return replaced

print play_game(list_of_sentences[ randint( 0, length_of_list-1 ) ], parts_of_speech)
