import re
def validIPAddress(self, IP: str) -> str:
    patternIPv4 = "^((([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9])).){3}(([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9]))$"
    patternIPv6 = "^([0-9a-fA-F]{1,4}[:]){7}[0-9a-fA-F]{1,4}$"
    if re.search(patternIPv4, IP):
        return "IPv4"
    elif re.search(patternIPv6, IP):
        return "IPv6"
    return "Neither"
