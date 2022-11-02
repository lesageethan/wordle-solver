import random

def getWordsList():
    wordsList = []
    with open('5words.txt', 'r') as words:
        for word in words:
            wordsList.append(word[:-1])
    return wordsList

def gameLoop():
    words = getWordsList()
    for i in range(0, 100):
        print('Possible words left:', len(words))
        if i==0:
            guess = 'BARES'
        else:
            guess = words[random.randint(0, len(words)-1)]
        print(guess)
        # 0=Not in, 1=In, 2=Correct
        feedback = input("Enter feedback:")
        if feedback!='X':
            words = eliminate(feedback, guess, words)

def eliminate(feedback, guess, words):
    for num in range(0, 5):
        digit = int(feedback[num])
        letter = guess[num]
        if digit==0:
            words = notin(letter, words)
        if digit==1:
            words = isin(letter, words)
            words = notthere(num, letter, words)
        if digit==2:
            words=isright(num, letter, words)
    return words

def notin(letter, words):
    newWords = []
    for word in words:
        if letter not in word:
            newWords.append(word)
    return newWords

def isin(letter, words):
    newWords = []
    for word in words:
        if letter in word:
            newWords.append(word)
    return newWords

def isright(location, letter, words):
    newWords = []
    for word in words:
        if word[location]==letter:
            newWords.append(word)
    return newWords

def notthere(location, letter, words):
    newWords = []
    for word in words:
        if word[location]!=letter:
            newWords.append(word)
    return newWords

gameLoop()


