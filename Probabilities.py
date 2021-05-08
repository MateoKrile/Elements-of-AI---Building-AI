import random

def main():

    favourite = 'dogs' if random.random() > 0.8 else 'cats' if random.random() > 0.1 else "bats"
    print("I love " + favourite) 

main()