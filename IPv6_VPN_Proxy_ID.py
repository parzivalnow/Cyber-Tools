import hashlib
import time
class IPv6_VPN_Proxy:
    def __init__(self):
        self.mapper = "abcdef0123456789"
        self.Database = {}

    def encode(self, ipv6: str) -> str:
        tagID = ""
        hash = hashlib.sha512()
        while tagID in self.Database.keys() or tagID == "":
            tagID = ""
            hash.update(str(time.time()).encode('utf-8'))
            string = hash.hexdigest()
            for i in range(0, len(string), 21):
                tagID += self.mapper[self.decodeHex2Int(string[i:i+33])%16]
        self.Database[tagID] = ipv6
        return tagID
            
    def decode(self, tagID: str) -> str:
        if tagID in self.Database.keys():
            return self.Database[tagID]
        return ""
    
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
    
    def returnDatabaseLength(self):
        return len(self.Database)