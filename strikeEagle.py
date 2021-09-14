# This assumes you have nmap installed on your Debian distribution

import subprocess

class osStrike:
    def __init__(self, ip, options = [], ports = []]):
        options = self.stringBuilder(ip, options, ports)
        self.cmd = subprocess.Popen(['nmap', options], stdout = subprocess.PIPE)

    def stringBuilder(self, ip, options, ports):
        try:
            string = " ".join(options)
            string += " " + ip 
            string += " -p " + ",".join(ports)
        except:
            return "-F " + ip

        return string

    def parseNmap(self):
        # Pass to geoHawk 2 totalVirus 2 OTX AlienVault
        pass

    def display(self):
        print(str(self.cmd.communicate()))
