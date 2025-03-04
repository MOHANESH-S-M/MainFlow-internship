# This is Task 6
""" 46. Word Ladder Problem
 Objective   : Given two words, find the shortest transformation sequence from the start
               word to the end word, changing only one letter at a time.
 Input       : Two words and a dictionary of words.
 Output      : The length of the shortest transformation sequence.
 Hint        : Use breadth-first search (BFS) and treat each word as a node in a graph."""
from collections import deque

def word_ladder_length(beginWord, endWord, wordList):
    wordSet = set(wordList) 
    if endWord not in wordSet:
        return 0 

    queue = deque([(beginWord, 1)])  

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps 
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                transformed_word = word[:i] + c + word[i+1:]

                if transformed_word in wordSet:
                    queue.append((transformed_word, steps + 1))
                    wordSet.remove(transformed_word) 

    return 0 
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print("Shortest transformation length:", word_ladder_length(beginWord, endWord, wordList))
