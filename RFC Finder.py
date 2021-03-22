################################################
# Reference used
# Ortega, J., Washington, S. (2019). Learning Python Networking - Second Edition. 
"""
try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)
template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc = requests.get(url).text
"""


################################################

import sys, urllib.request, re
class RFCsearch:
    
    def __init__(self, searchDict, threshold = 700, lower = None, upper = None):
        self.lowerNumber = lower
        self.upperNumber = upper
        self.searchDict = searchDict
        self.threshold = threshold
    
    def generateRFCs(self):
        if self.lowerNumber != None and self.upperNumber != None:
            rfcList = []
            try:
                for i in range(self.lowerNumber, self.upperNumber + 1):
                    try:
                        if self.getRFCScore(i) != -1:
                            rfcList.append(i)
                    except:
                        continue
            except:
                print("Failed during process execution.")
            return rfcList
        elif self.lowerNumber != None:
            try:
                if self.getRFCScore(self.lowerNumber) != -1:
                    return self.lowerNumber
            except:
                print("Failed during process execution.")
        return -1
        
    def getRFCScore(self, number):
        if number != None:
            try:
                rfc_number = int(number)
            except (IndexError, ValueError):
                print("Must supply an RFC number as first argument")
                sys.exit(2)
            template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
            url = template.format(rfc_number)
            rfc_raw = urllib.request.urlopen(url).read()
            rfc = rfc_raw.decode()
            if self.scoreRFC(rfc) >= self.threshold:
                return number
        return -1
    
    def scoreRFC(self, rfc):
        score = 0
        docDict = {}
        for line in rfc.split():
            if line in docDict.keys():
                docDict[line] += 1
            else:
                docDict[line] = 1

        for val in searchDict:
            pattern = '.*(' + val + '|' + val.upper() + '|' + val.capitalize() + '|' + val.lower() + ').*'
            for key in docDict.keys():
                if re.search(pattern, key):
                    score += self.searchDict[val] * docDict[key]
        return score
    
    def viewRFC(self, number):
        try:
            rfc_number = int(number)
        except (IndexError, ValueError):
            print("Must supply an RFC number as first argument")
            sys.exit(2)
        template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
        url = template.format(rfc_number)
        rfc_raw = urllib.request.urlopen(url).read()
        print(rfc_raw.decode())
