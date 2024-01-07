import random

def greet():
    index = random.randint(0,2) % 3
    if index == 0:
        print("Hello")
    elif index ==1:
        print("How do you do")
    else:    
        print("Hows it going")

greet()