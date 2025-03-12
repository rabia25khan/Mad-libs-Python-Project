# MadLibs Game - Funny Adventure!

# User inputs
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
food = input("Enter a type of food: ")

# MadLib story
madlib = f"""
Yesterday, I went to {place} and saw a very {adjective} {animal}. 
It started to {verb1} around and then suddenly began to {verb2}! 
I was so surprised that I dropped my {food} on the ground. 
What a crazy day it was!
"""

# Print the funny story
print("\n--- Your Funny Story ---")
print(madlib)
