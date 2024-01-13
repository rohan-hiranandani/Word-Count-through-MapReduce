base = []

def shuffleSort():
    combinedData = " ".join(base)
    wordList = {}
    
    for word in combinedData.split():
        word = word.strip("(").split(",")[0]
        wordList[word] = wordList.get(word, 0) + 1
    
    return wordList
