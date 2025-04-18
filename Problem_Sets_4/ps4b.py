# Problem Set 4B
# Name:
# Collaborators:

import random


class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            the message text
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        self.message_text = input_text

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''Message('{self.get_text()}')'''

    def get_text(self):
        '''
        Used to access the message text outside of the class

        Returns: (string) the message text
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        return self.message_text

    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char by

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        asci_char = ord(char) - 32
        # 32 - 32 = 0  126 - 32 = 94
        asci_shift_char = (asci_char + shift) % 95 + 32
        shifted_char = chr(asci_shift_char)
        return shifted_char

    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to the message text.
        For each character in the text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt the message text
                        len(pad) == len(the message text)

        Returns: (string) The ciphertext produced using the one time pad
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        s = ""
        t = self.get_text()
        for i in range(len(pad)):
            s += self.shift_char(t[i], pad[i])
        return s

# a = "Monoo#"
# m = Message(a)
# l = [5, 10, 2, 3, 0, 2]
# l = [-l[i] for i in range(len(l))]
# print(l)
# b = m.apply_pad(l)
# print(b)

class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad is not None then len(pad) == len(self.input_text)

        A PlaintextMessage object inherits from Message. It has three attributes:
            the message text
            the pad (list of integers, determined by pad
                or generated randomly using self.generate_pad() if pad is None)
            the ciphertext (string, input_text encrypted using the pad)
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        super().__init__(input_text)
        if pad == None:
            self.pad = self.generate_pad().copy()
        else:
            self.pad = pad.copy()
        self.ciphertext = self.apply_pad(self.pad)
            
    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''PlaintextMessage('{self.get_text()}', {self.get_pad()})'''

    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt the message text.

        The pad should be generated by making a new list and for each character
            in the message chosing a random number in the range [0, 110) and
            adding that number to the list.

        Returns: (list of integers) the new one time pad
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        g_pad = []
        l = len(self.get_text())
        for i in range(l):
            g_pad.append(random.randint(0, 109))
        return g_pad

    def get_pad(self):
        '''
        Used to safely access your one time pad outside of the class

        Returns: (list of integers) a COPY of your pad
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        return self.pad.copy()

    def get_ciphertext(self):
        '''
        Used to access the ciphertext produced by applying pad to the message text

        Returns: (string) the ciphertext
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        return self.apply_pad(self.get_pad())

    def change_pad(self, new_pad):
        '''
        Changes the pad used to encrypt the message text and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(new_pad) == len(the message text)

        Returns: nothing
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        self.pad = new_pad

class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has one attribute:
            the message text (ciphertext)
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        super().__init__(input_text)
        

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''EncryptedMessage('{self.get_text()}')'''

    def decrypt_message(self, pad):
        '''
        Decrypts the message text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(the message text)

        Returns: (PlaintextMessage) the decrypted message (containing the pad)
        '''
        # raise NotImplementedError  # delete this line and replace with your code here
        n_pad = [-pad[i] for i in range(len(pad))]
        p = PlaintextMessage(self.get_text(), pad)
        p.message_text = self.apply_pad(n_pad)
        return p