from math import log2
import string, json, itertools, functools, time

#generating combinations
# import itertools
# choices = ["a","g","gr"]
# _choices = [choices]*5
# combinations = [p for p in itertools.product(*_choices)]

def parseWords(filename):
    returnList = []
    with open(filename, "r") as f:
        for line in f:
            returnList.append(line[:-1])
    return returnList

def writeToJson(filename,data):
    with open(filename, "w") as f:
        jsonStr = json.dumps(data)
        f.write(jsonStr)

def readFromJson(filename):
    with open(filename, "r") as f:
        return json.load(f)

#CREATES ALPHABET OF LETTER FREQUENCIES
def createAlphabet():
    alphabet = {}
    for char in string.ascii_lowercase:
        alphabet[char] = [0,0,0,0,0,0]

    for i in allowedWords:
        for j in range(5):
            alphabet[i[j]][j] += 1

    for i in alphabet.keys():
        for j in allowedWords:
            if i in j:
                alphabet[i][5] += 1
    return alphabet

#key for sorting word list
def sortKey(e):
    return e[1]

allowedWords = parseWords("allowed_words.txt")
possibleWords = parseWords("possible_words.txt")

alphabet = createAlphabet()

#INITIALISING DICT
#allowedWordsDict = {}

# for word in allowedWords:
#     allowedWordsDict[word] = (0,0)
# writeToJson('data.json', allowedWordsDict)

#CALCULATING COMBINATIONS
# _choices = [["amb","grn","gry"]]*5
# combinations = [p for p in itertools.product(*_choices)]
# combDict = {}
# for combination in combinations:
#     _string = ""
#     for char in combination:
#         _string += char + "-"
#     _string = _string[:-1]
#     combDict[_string] = (0,0)
# for enum in enumerate(allowedWords):
#     allowedWordsDict[enum[1]][1] = combDict

#CALCULATING PROBABILITIES
# for word in allowedWords:
#     combinations = allowedWordsDict[word][1]
#     for combination in combinations:
#         _combination = combination.split("-")
#         combinationP = [0,0,0,0,0]
#         for enum in enumerate(_combination):
#             if enum[1] == "grn":
#                 combinationP[enum[0]] = alphabet[word[enum[0]]][enum[0]]/12972
#             elif enum[1] == "amb":
#                 combinationP[enum[0]] = (alphabet[word[enum[0]]][5]/12972)-(alphabet[word[enum[0]]][enum[0]]/12972)
#             elif enum[1] == "gry":
#                 combinationP[enum[0]] = (12972 - alphabet[word[enum[0]]][5])/12972
#             combinations[combination][1] = functools.reduce(lambda a,b : a*b, combinationP)
#     #print(word)

#CALCULATING BITS
# for word in allowedWords:
#     combinations = allowedWordsDict[word][1]
#     for combination in combinations:
#         combinations[combination][0] = -log2(combinations[combination][1])

#CALCULATING ENTROPY
# for word in allowedWords:
#     combinations = allowedWordsDict[word][1]
#     sum = 0
#     for combination in combinations:
#         sum += combinations[combination][0]*combinations[combination][1]
#     allowedWordsDict[word][0] = sum

timeNow = time.time()
allowedWordsDict = readFromJson("data.json")
#print(allowedWordsDict)
#writeToJson('data.json', allowedWordsDict)

calculatedWords = []
for word in allowedWords:
    calculatedWords.append((word, allowedWordsDict[word][0]))
calculatedWords.sort(reverse=True,key=sortKey)
print(calculatedWords)

with open("calculatedWords.txt", "w") as f:
    for word in calculatedWords:
        f.write(word[0] + " " + str(word[1]) + "\n")

print(f"runtime was {time.time()-timeNow} seconds")