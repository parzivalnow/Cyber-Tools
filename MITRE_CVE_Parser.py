import sys, urllib.request, re
from bs4 import BeautifulSoup
from urllib.request import urlopen

def scoreMITRE_CVEs(homePageAbstract):
        score = 0
        abstractDict = {}
        for line in homePageAbstract.split():
            if line in abstractDict.keys():
                abstractDict[line] += 1
            else:
                abstractDict[line] = 1

        for val in scoreCard.keys():
            pattern = '.*(' + val + '|' + val.upper() + '|' + val.capitalize() + '|' + val.lower() + ').*'
            for key in abstractDict.keys():
                if re.search(pattern, key):
                    score += scoreCard[val] * abstractDict[key] 
        return score
    

##########################################
# Reference used
# Sweigart, A. (2018). Cracking Codes with Python: An Introduction to Building and Breaking Ciphers. http://inventwithpython.com/cracking/
##########################################

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
def loadDictionary():
    dictionaryFile = open('english_wordDict.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None

    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0 # no words at all, so return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)
def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)
def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch

def findText(soup):
    td = soup.findAll('td')
    for i in td:
        for x in i:
            try:
                if isEnglish(x) == True and len(x) > 100:
                    return x
            except:
                continue
                
                
                
##########################################
# Reference use
# Amos, D. (2020). A Practical Introduction to Web Scraping in Python. https://realpython.com/python-web-scraping-practical-introduction/
##########################################

def CVEparser(scoreCard, threshold):
    url_MITRE_Validator = '^/cgi-bin/cvename.cgi[?]name=CVE-[0-9]{4}-[0-9]{4,}$'
    links = []
    template = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword="
    searches = ["linux", "root", "privilege"]
    baseUrl = template + "+".join(searches)
    page = urlopen(baseUrl)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        if re.search(url_MITRE_Validator, link["href"]):
            testPage = urlopen("https://cve.mitre.org"+link["href"])
            testHtml = testPage.read().decode("utf-8")
            testSoup = BeautifulSoup(testHtml, "html.parser")
            words = findText(testSoup)
            if scoreMITRE_CVEs(words) > threshold:
                links.append("https://cve.mitre.org"+link["href"])
    return links