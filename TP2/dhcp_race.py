from scapy.all import *

def handle(pkt):
    if DHCP not in pkt or pkt[DHCP].options[0][1] != 1:
        return
    mac = pkt[Ether].src
    offer = (Ether(src="aa:aa:aa:aa:aa:aa", dst=mac) /
             IP(src="10.1.10.200", dst="255.255.255.255") /
             UDP(sport=67, dport=68) /
             BOOTP(op=2, yiaddr="10.1.10.251", siaddr="10.1.10.200", chaddr=bytes.fromhex(mac.replace(":", ""))) /
             DHCP(options=[("message-type","offer"),("server_id","10.1.10.200"),("router","10.1.10.254"),("dns","1.1.1.1"),("subnet_mask","255.255.255.0"),"end"]))
    sendp(offer, iface="eth0", verbose=False)
    print(f"offer envoye a {mac}")

sniff(iface="eth0", filter="udp and port 67", prn=handle, store=0)