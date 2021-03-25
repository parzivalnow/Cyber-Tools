
###################################
# Reference use
# Amos, D. (2020). A Practical Introduction to Web Scraping in Python. https://realpython.com/python-web-scraping-practical-introduction/
###################################

import sys, urllib.request, re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# A typical article url looks like the following: https://krebsonsecurity.com/2021/03/phish-leads-to-breach-at-calif-state-controller/
krebsOnSecurityValidator = "^https://krebsonsecurity.com/[12]{1}[0-9]{3}/[0-9]{2}.*/$" 

def scoreKrebsSecurity(scoreCard, homePageAbstract):
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
      
      
def KrebsWorkhorse(url):
    url = urlopen(url)
    html = url.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    testLinks = []
    for link in soup.find_all("a"):
        try:
            if re.search(krebsOnSecurityValidator, link["href"]) and link["href"] not in testLinks:
                testLink = link["href"]
                testPage = urlopen(testLink)
                testHtml = testPage.read().decode("utf-8")
                testSoup = BeautifulSoup(testHtml, "html.parser")
                testScore = 0
                for words in testSoup.find_all("p"):
                    for line in words:
                        try:
                            testScore += scoreKrebsSecurity(scoreCard, line)
                        except:
                            continue
                if testScore >= 25:
                    testLinks.append(testLink)
        except:
            continue
    return testLinks
  
def parseKrebsOnSecurity(pages):
    testLinks = []
    baseUrl = "https://krebsonsecurity.com/"
    # In order to match extra pages we need the following form: https://krebsonsecurity.com/page/4/
    for page in range(1, pages+1):
        if page == 1:
            url = baseUrl
        else:
            url = baseUrl + "/page/" + str(page) + "/"
        for link in KrebsWorkhorse(url):
            testLinks.append(link)
        
    return testLinks
  
