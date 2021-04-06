class LogSystem:

    def __init__(self):
        self.users = {}

    def put(self, id: int, timestamp: str) -> None:
        if id not in self.users.keys():
            self.users[id] = [timestamp]
        else:
            self.users[id].append(timestamp)
            self.users[id] = sorted(self.users[id])
                

    def retrieve(self, start: str, end: str, g: str) -> List[int]:
        startIdx = 4
        if g == "Month":
            startIdx += 2
        elif g == "Day":
            startIdx += 4
        elif g == "Hour":
            startIdx += 6
        elif g == "Minute":
            startIdx += 8
        elif g == "Second":
            startIdx += 10

        start = int(start.replace(":","")[:startIdx])
        end = int(end.replace(":", "")[:startIdx])
        
        returnUIDs = []
        
        for UID, times in self.users.items():
            for time in times:
                time = int(time.replace(":", "")[:startIdx])
                if time >= start and time <= end:
                    returnUIDs.append(UID)
                    break
        
        return returnUIDs
