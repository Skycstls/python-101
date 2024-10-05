#pribando scapy

from scapy.all import send, IP, ICMP

send(IP(dst="google.com")/ICMP())