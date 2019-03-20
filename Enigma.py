#!/usr/bin/python3

import string

wheel_count = 3

wheels = [("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "R"),
          ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "F"),
          ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "W"),
          ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "K"),
          ("VZBRGITYUPSDNHLXAWMJQOFECK", "A"),
          ("JPGVOUMFYQBENHZRDKASXLICTW", "AN"),
          ("NZJHGRCXMYSWBOUFAIVLPEKQDT", "AN"),
          ("FKQHTLXOCBJSPDZRAMEWNIUYGV", "AN")]

reflectors = ["EJMZALYXVBWFCRQUONTSPIKHGD",
              "YRUHQSLDPXNGOKMIEBFZCWVJAT",
              "FVPJIAOYEDRZXWGCTKUQSBNMHL"]

class Wheel:
    """A wheel class to hold the input and output strings,
       with the ability to rotate its string an arbitrary
       amount, and to encode and reverse encode a character"""

    def __init__(self, sequence, notches):
        self.input = string.ascii_uppercase
        self.output = sequence
        self.notches = notches

    def rotate(self, amount = 1):
        """Simulate a cylinder rotating"""
        self.input = self.input[amount:] + self.input[:amount]
        self.output = self.output[amount:] + self.output[:amount]

    def notch_active(self):
        """If the first character of the input string is one of the
           characters in the self.notches string, return True, else False"""
        return self.input[0] in self.notches

    def encode(self, char, reverse=False):
        temp = self.input[string.ascii_uppercase.index(char)]
        if not reverse:
            temp = self.output[self.input.index(temp)]
        else:
            temp = self.input[self.output.index(temp)]
        temp = string.ascii_uppercase[self.input.index(temp)]
        return temp                

def get_wheel_choices():
    """Gets a list of 0-based integers which is wheel_count items 
       long from the user. Validates input, and re-asks if the user
       gives a nonsense answer"""

    wheel_choices = []

    while len(wheel_choices) < wheel_count:
        choice_number = len(wheel_choices) + 1
        choice = input("Please type a wheel number for slot %d, 1-8: " % choice_number)

        if len(choice) == 1 and choice in string.digits and int(choice) in range(1,9):
            wheel_choices.append(int(choice)-1)
        else:
            print("That was an invalid choice")

    return wheel_choices

def get_wheel_settings():
    """Asks the user for a-z choices for wheel settings, returning a list of
       wheel_count length, with 0-based integers denoting the a-z positions
       chosen by the user"""

    wheel_settings = []
    
    while len(wheel_settings) < wheel_count:
        choice_number = len(wheel_settings) + 1
        choice = input("Please type a setting for wheel %d, a-z: " % choice_number)

        choice = choice.upper()
        if len(choice) == 1 and choice in string.ascii_uppercase:
            wheel_settings.append(string.ascii_uppercase.index(choice))
        else:
            print("That was an invalid choice")

    return wheel_settings

def get_reflector():
    """Asks the user a, b, or c reflector, and returns 0, 1, or 2"""

    while True:
        choice = input("Please choose a reflector, a, b, or c: ")
        if choice in "abc":
            return "abc".index(choice)
        else:
            print("That was an invalid choice")

def get_message():
    """Get the users input message. Don't allow characters other than a-z"""

    while True:
        message = input("Please enter the message to encrypt: ").upper()
        for char in message:
            if char not in string.ascii_uppercase:
                print("That was an invalid message. Only characters a-z are supported")
                break
        else:
            return message

def encrypt(working_wheels, wheel_settings, working_reflector, message):
    for i in range(len(working_wheels)):
        w = working_wheels[i]
        s = wheel_settings[i]
        w.rotate(s)

    # Now for the fun bit
    encrypted = []
    for char in message:
        #Rotate wheels if the notches are active
        working_wheels[2].rotate()
        if working_wheels[2].notch_active():
            working_wheels[1].rotate()
            if working_wheels[1].notch_active():
                working_wheels[0].rotate()

        #FIXME Plugboard is missing entirely

        #Encode with each wheel, in reverse order
        for i in range(len(working_wheels)-1, -1, -1):
            char = working_wheels[i].encode(char)
        
        #Encode with the reflector
        char = working_reflector[string.ascii_uppercase.index(char)]

        #"Reverse" Encode with each wheel in standard order
        for i in range(len(working_wheels)):
            char = working_wheels[i].encode(char, reverse=True)

        #FIXME Plugboard would happen here too

        #Save the encrypted character
        encrypted.append(char)

    return "".join(encrypted)

def main():
    """Gather the users wheel choices, settings, reflector choice and message,
       encrypt the message, and print the result to the screen"""
    wheel_choices = get_wheel_choices()
    wheel_settings = get_wheel_settings()
    reflector_choice = get_reflector()
    message = get_message()

    # wheel_choices is a list of ints, turn it into a list of tuples. Each
    # tuple has the connections (relative to a standard alphabet) in string format,
    # and the notch positions as a second string in the tuple
    working_wheels = [Wheel(wheels[i][0], wheels[i][1]) for i in wheel_choices]

    # Take the integer reflector_choice and make us a working copy of that reflector
    working_reflector = reflectors[reflector_choice]

    # The meat and potatoes
    encrypted = encrypt(working_wheels, wheel_settings, working_reflector, message)

    print("Your encrypted text:", encrypted)

if __name__ == "__main__":
    main()
