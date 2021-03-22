###################################
# Reference use
# Amos, D. (2020). A Practical Introduction to Web Scraping in Python. https://realpython.com/python-web-scraping-practical-introduction/
###################################

import sys, urllib.request, re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from GenerateDateRange import generateDateRange
from GeneratePrevDay import generatePrevDay


def scoreHackerNews(homePageAbstract):
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
    
    
def HackerNewsParser(days, scoreCard, threshold):
    urlValidator = '^https://thehackernews.com/.*'
    links = []
    for date in generateDateRange(5):
        template = "https://thehackernews.com/search?updated-max={}T07:04:00-08:00&max-results=1500&start=1&by-date=false"
        baseUrl = template.format(date)
        page = urlopen(baseUrl)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a"):
            if len(link.text) > 50 and re.search(urlValidator, link["href"]):
                testLink = link["href"]
                testPage = urlopen(testLink)
                testHtml = testPage.read().decode("utf-8")
                testSoup = BeautifulSoup(testHtml, "html.parser")
                testScore = 0
                for words in testSoup.find_all("p"):
                    for line in words:
                        try:
                            testScore += scoreHackerNews(line)
                        except:
                            continue
                if testScore >= 25 and testLink not in links:
                    links.append(testLink)
    return links