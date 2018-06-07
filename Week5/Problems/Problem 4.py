from ps6 import *

def decrypt_story(story):
    a = Message.CiphertextMessage(story)
    return a.decrypt_message(story)

print(decrypt_story(get_story_string()))