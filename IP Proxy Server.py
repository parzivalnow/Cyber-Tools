import hashlib
import time
import re
class VPN_Proxy:
    def __init__(self):
        self.mapper = "abcdef0123456789"
        self.Database = {}

    def encode(self, ip: str) -> str:
        ipType = self.validIPAddress(ip)
        if ipType == 'Neither':
            raise Exception("NOT VALID IP")
        tagID = ""
        hash = hashlib.sha512()
        while tagID in self.Database.keys() or tagID == "":
            tagID = ""
            hash.update(str(time.time()).encode('utf-8'))
            string = hash.hexdigest()
            for i in range(0, len(string), 21):
                tagID += self.mapper[self.decodeHex2Int(string[i:i+33])%16]
        self.Database[tagID] = ip
        return tagID
            
    def decode(self, tagID: str) -> str:
        if tagID in self.Database.keys():
            return self.Database[tagID]
        return ""
    
    def signingOff(self, tagID):
        if tagID in self.Database.keys():
            del self.Database[tagID]
    
    def decodeHex2Int(self, hexcode):
        dictionary = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
        ints = 0
        for x in range(0, len(hexcode)):
            i = hexcode[x]
            if i != ":":
                first = i.lower()
                if first in dictionary.keys():
                    first = dictionary[first]
                ints += int(first)
        return ints
    
    def validIPAddress(self, IP: str) -> str:
        patternIPv4 = "^((([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9])).){3}(([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9]))$"
        patternIPv6 = "^([0-9a-fA-F]{1,4}[:]){7}[0-9a-fA-F]{1,4}$"
        if re.search(patternIPv4, IP):
            return "IPv4"
        elif re.search(patternIPv6, IP):
            return "IPv6"
        return "Neither"

    def returnDatabaseLength(self):
        return len(self.Database)