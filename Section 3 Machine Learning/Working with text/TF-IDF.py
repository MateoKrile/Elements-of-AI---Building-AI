"""
Let's combine two tasks: finding the most similar pair of lines and the tf-idf representation.

Write a program that uses the tf-idf vectors to find the most similar pair of lines in a given data set. 
You can test your solution with the example text below. Note, however, that your solution will be tested on other data sets too, 
so make sure you don't make use of any special properties of the example data (like there being four lines of text).

This exercise requires a bit more work than average but you should be able to benefit from what you have done in the previous exercises. 
Make sure to revisit them in case you feel like you need a refresher.
"""
import numpy as np
from numpy.core.numeric import Inf

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''
docs = [line.lower().split() for line in text.split('\n')]


def manhattan_dist(a, b):
    dist = 0
    for ai, bi in zip(a, b):
        dist += abs(ai - bi)
    return dist

def unique_words(docs):
    words = set()
    for doc in docs:
        for word in doc:
            words.add(word)
    return words

def main(text):
    docs = [line.lower().split() for line in text.split('\n')]
    words = unique_words(docs)
    N = len(docs)
    # term frequency matrix
    tf = [{word:0 for word in words} for _ in range(N)]
    # Inverse document frequency matrix
    df = {word:0 for word in words}
    
    for i, doc in enumerate(docs):
        for word in doc:
            tf[i][word] += 1.0/len(doc)
            df[word] += 1.0/N
   
    tf_idf = [{word:0 for word in words} for _ in range(N)]
    for i, doc in enumerate(docs):
        for word in doc:
            tf_idf[i][word] = tf[i][word] * np.math.log10(N/(df[word]+1))
    
    dist = np.empty((N, N), dtype = np.float)
    for x in range(len(tf_idf)):
        for y in range(len(tf_idf)):
            if x==y:
                dist[x][y] = np.Inf
            else:
                dist[x][y] = manhattan_dist(tf_idf[x].values(), tf_idf[y].values())

    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)