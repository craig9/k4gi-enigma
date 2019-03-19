# k4gi's Enigma Machine

This is a fork of k4gi's Enigma Machine, and I'm just playing with it to try to figure out how it works.


## To compile:

1. $ sudo apt install openjdk-11-jdk
2. $ javac Cipher3.java (Ignore the warnings - for now)
3. $ java Cipher3

## K4gi's notes from the code

### About the stepping mechanism

Gotta say a little bit about the stepping mechanism.
Rotors I-V  have one step, rotors VI-VIII have two.
The thing is they're written down as the place on the entry character
so I guess I do need to keep track of both after all
come to think of it why did I think I didn't? Of course I need to know where its turned to!
Anyway. Yes.
I'm just going to write them down right now as A-B, meaning when A clicks to B

### About the mechanism generally

Here is a paper enigma machine in action.

[![Paper enigma machine in action](http://img.youtube.com/vi/pZsuxZXN33g/0.jpg)](https://www.youtube.com/watch?v=pZsuxZXN33g)

Notice that the wheels, rotors, whatever, move BEFORE encoding the letter typed!
            
The Enigma machine works by sending an electrical signal along this path:

1. Input character (to plugboard and then static wheel?)
2. Shift rotors
3. Plugboard
4. Wheel III
5. Wheel II
6. Wheel I
7. Reflector
8. Wheel I
9. Wheel II
10. Wheel III (then static wheel?)
11. Plugboard (then lampboard?)
12. Output character

(in some versions there are four wheels)

Wheel specs are recorded here:
* [https://en.wikipedia.org/wiki/Enigma_rotor_details] (has more rotors than the others)
* [http://users.telenet.be/d.rijmenants/en/enigmatech.htm] (Where we take the reflector wheel info from)
* [https://www.codesandciphers.org.uk/enigma/rotorspec.htm]

