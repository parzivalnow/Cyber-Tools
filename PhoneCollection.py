import time
import random
class PhoneCounter:
    def __init__(self):
        self.phones = {}
        
    def hit(self, number, timestamp):
        if number not in self.phones.keys():
            self.phones[number] = [timestamp]
        else:
            self.phones[number].append(timestamp)
            
    def getHits(self, timestamp, selector = None, duration = 300):
        if len(self.phones.keys()) == 0:
            return 0
        
        if selector == None:
            hits = 0
            for key, val in self.phones.items():
                ptr = len(val)-1
                while ptr >= 0 and abs(timestamp-val[ptr]) <= duration:
                    hits += 1
                    ptr -= 1
            return hits
        elif selector in self.phones.keys():
            hits = 0
            for val in self.phones[selector]:
                if abs(timestamp-val) <= duration:
                    hits += 1
            return hits
    
    def getSelector(self, number, timestamp = None, duration = 300):
        number = str(number)
        if number in self.phones.keys():
            try:
                if abs(timestamp-self.phones[number][-1]) <= duration:
                    return [x for x in self.phones[number] if abs(timestamp-x) <= duration]
                else:
                    return self.phones[number]
            except:
                return "Error"
        return "No selector here!"
    
    def database(self, number = None):
        if number == None:
            return self.phones.items()
        elif number in self.phones.keys():
            return self.phones[number]
        else:
            return "Number not found!"