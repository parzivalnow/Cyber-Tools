#include <regex>
string validIPAddress(string IP) {
    regex patternIPv4("^((([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9])).){3}(([1]?[1-9]?[0-9])|([2][0-4][0-9])|([2][0-5][0-5])|([1][0-9][0-9]))$");
    regex patternIPv6("^([0-9a-fA-F]{1,4}[:]){7}[0-9a-fA-F]{1,4}$");
    if (regex_match(IP, patternIPv4)){
        return "IPv4";
    } else if (regex_match(IP, patternIPv6)){
        return "IPv6";
    } else{
        return "Neither";
    }
}
