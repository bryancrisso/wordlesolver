import string, json

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

allowedWords = parseWords("allowed_words.txt")
possibleWords = parseWords("possible_words.txt")

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

allowedWordsDict = {}

for word in allowedWords:
    allowedWordsDict[word] = (0,0)

writeToJson("data.json", allowedWordsDict)
print(readFromJson("data.json"))