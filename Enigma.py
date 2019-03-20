#!/usr/bin/python3

import string

debugging = True

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
    def __init__(self, sequence, ticks):
        self.input = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.output = sequence
        self.ticks = ticks

    def rotate(self, amount = 1):
        self.input = self.input[amount:] + self.input[:amount]
        self.output = self.output[amount:] + self.output[:amount]

    def __str__(self):
        return self.input + " / " + self.output + " / " + self.ticks

    def tick_activated(self):
        return self.input[0] in self.ticks

    def encode(self, char, reverse=False):
        temp = self.input[string.ascii_uppercase.index(char)]
        if not reverse:
            temp = self.output[self.input.index(temp)]
        else:
            temp = self.input[self.output.index(temp)]
        temp = string.ascii_uppercase[self.input.index(temp)]
        return temp                

def get_wheel_choices():
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
    while True:
        choice = input("Please choose a reflector, a, b, or c: ")
        if choice in "abc":
            return "abc".index(choice)
        else:
            print("That was an invalid choice")

def get_message():
    while True:
        message = input("Please enter the message to encrypt: ").upper()
        for char in message:
            if char not in string.ascii_uppercase:
                print("That was an invalid message. Only characters a-z are supported")
                break
        else:
            return message

def main():
    wheel_choices = get_wheel_choices()
    wheel_settings = get_wheel_settings()
    reflector_choice = get_reflector()
    message = get_message()
    print("Thank you")
    print()

    working_wheels = [Wheel(wheels[i][0], wheels[i][1]) for i in wheel_choices]
    working_reflector = reflectors[reflector_choice]

    for i in range(len(working_wheels)):
        w = working_wheels[i]
        s = wheel_settings[i]
        w.rotate(s)

    # Now for the fun bit
    encrypted = []
    for char in message:
        working_wheels[2].rotate()
        if working_wheels[2].tick_activated():
            working_wheels[1].rotate()
            if working_wheels[1].tick_activated():
                working_wheels[0].rotate()

        #FIXME Plugboard is missing entirely

        for i in range(len(working_wheels)-1, -1, -1):
            char = working_wheels[i].encode(char)
        
        char = working_reflector[string.ascii_uppercase.index(char)]

        for i in range(len(working_wheels)):
            char = working_wheels[i].encode(char, reverse=True)

        #FIXME Plugboard would happen here too

        encrypted.append(char)

    print("Your encrypted text:", "".join(encrypted))

if __name__ == "__main__":
    main()
