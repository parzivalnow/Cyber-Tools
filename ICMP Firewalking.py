import time
class ICMP_FirewalkingDB:
    def __init__(self, dataRetention = "Forever"): 
        # Data Retention can be Forever, 6 months, 1 month, or 1 week
        self.map = {}
        if dataRetention in ["6 months", "1 month", "1 week"]:
            if dataRetention == "6 months":
                #60*60*24*180
                self.dataRetention = 15552000
            elif dataRetention == "1 month":
                #60*60*24*30
                self.dataRetention = 2592000
            else:
                #60*60*24*7
                self.dataRetention = 604800
        else:
            self.dataRetention = "Forever"

    def cleanDB(self, currentTime):
        if len(self.map) > 0 and self.dataRetention != "Forever":
            items = list(self.map.items())
            for item in items:
                if len(item[1]) > 1:
                    newList = []
                    for event in item[1]:
                        if (currentTime-event[2]) <= self.dataRetention:
                            newList.append(event)
                    if len(newList) == 0:
                        del self.map[item[0]]
                    else:
                        self.map[item[0]] = newList
                else:
                    if (currentTime-item[1][0][2]) >= self.dataRetention:
                        del self.map[item[0]]
        
    def update(self, router, timeToLive, ICMPcode, currentTime):
        if router not in self.map.keys():
            self.map[router] = [[timeToLive, ICMPcode, currentTime]]
        else:
            self.map[router].append([timeToLive, ICMPcode, currentTime])

    def returnDatabase(self, router = None):
        if router != None:
            if router in self.map.keys():
                return self.map[router]
            else:
                return router + " not found!"
        else:
            return self.map