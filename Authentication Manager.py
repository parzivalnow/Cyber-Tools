class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.map = {}
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map.keys():
            if (currentTime - self.map[tokenId]) >= self.timeToLive:
                del self.map[tokenId]
            else:
                self.map[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        if len(self.map) > 0:
            count = 0
            items = list(self.map.items())
            for item in items:
                if item[0] in self.map.keys():
                    if (currentTime - item[1]) >= self.timeToLive:
                        del self.map[item[0]]
                    else:
                        count += 1
            return count
        return 0


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
