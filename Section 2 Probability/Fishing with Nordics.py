'''
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

Write a function that uses the above numbers and tries to guess the nationality 
of the winner when we know that the winner is a fisher and their gender (either female or male).

The argument of the function should be the gender of the winner ('female' or 'male'). 
The return value of the function should be a pair (country, probability) where country is the most 
likely nationality of the winner and probability is the probability of the country being the nationality of the winner.
'''
countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers
    all_fishers = sum(fishers)
    guess = None
    biggest = 0.0
    for i in range(len(countries)):
        prob = fishers[i]/all_fishers
        biggest, guess = (prob,countries[i]) if prob>biggest else (biggest, guess)
    return (guess, biggest*100)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()