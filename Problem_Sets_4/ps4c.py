# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    # raise NotImplementedError  # delete this line and replace with your code here
    word_list = load_words("words.txt")
    
    p_list = []
    for pad in pads:
        p = ciphertext.decrypt_message(pad)
        p_list.append(p)
    # print(p_list)
    
    plain_list = []
    for p in p_list:
        plain = p.get_text().split(" ")
        plain_list.append(plain)
    # print(plain_list)
    
    count_list = []
    for plain in plain_list:
        count = 0
        for e in plain:
            if is_word(word_list, e):
                count += 1
        count_list.append(count)
    # print(count_list)
    
    index = 0
    max_valid = max(count_list)
    for i in range(len(count_list)):
        if count_list[i] == max_valid:
            index = i
    # print(pads[index])
    ans = ciphertext.decrypt_message(pads[index])
    return ans
        

def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    # raise NotImplementedError  # delete this line and replace with your code here
    original_story = get_story_string()
    pads = get_story_pads()
    
    ciphertext_story = ps4b.EncryptedMessage(original_story)
    decoded = decrypt_message_try_pads(ciphertext_story, pads)
    return decoded.get_text()

if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    # pass