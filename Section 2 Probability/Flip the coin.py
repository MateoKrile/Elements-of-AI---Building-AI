'''
Write a program that generates 10000 random zeros and ones where the probability of one is p1 
and the probability of zero is 1-p1 (hint: np.random.choice([0,1], p=[1-p1, p1], size=10000)), 
counts the number of occurrences of 5 consecutive ones ("11111") in the sequence, 
and outputs this number as a return value. Check that for p1 = 2/3, the count is close to 10000 x (2/3)^5 ≈ 1316.9.
'''
import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

#Count the number of 11111 patterns in the generated filp list    
def count(seq):
    i = 0
    cnt = 0
    while i<len(seq)-1:
        if seq[i] and i+4<len(seq):
            ones = 1
            for j in range(1, 5):
                if seq[i+j]:
                    ones += 1
            if ones==5:
                cnt += 1
        i+=1
    return cnt

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
