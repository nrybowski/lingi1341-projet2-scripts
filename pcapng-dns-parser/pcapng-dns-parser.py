"""
Copyright (C) 2017  Nicolas Rybowski

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

#from pcapng import FileScanner
#from pcapng.blocks import EnhancedPacket

from scapy.all import *
from sys import argv, stdout, exit

if len(argv) != 3:
    msg = "Error :: Wrong arguments number : %i/3" %(len(argv))
    print msg
    exit()

input_file = str(argv[1])
outpout_file = str(argv[2])

msg = "Input file: '%s'\n" %(input_file)
msg += "Output file: %s" %(outpout_file)
print msg

a_pkt = 0
t_pkt = 0
ty = ""

with open(str(argv[2]), "w") as fd:
    with PcapReader('s1_c1.pcapng') as pcap_reader:
      for pkt in pcap_reader:
          t_pkt += 1

          """ Specifing dport and sport allows to avoid the MDNS packets (on port 5353) """
          if pkt.haslayer(DNS) and pkt.haslayer(IP) and (pkt.dport==53 or pkt.sport==53) and isinstance(pkt.an, DNSRR):
              a_pkt += 1
              t = pkt.qd.qtype

              if t == 1:
                  ty = "A"
              elif t == 28:
                  ty = "AAAA"

              #qst = "Query: %s \t\t:: Type: %s" %(pkt.qd.qname, ty)
              #print qst

              s1 = "%s,%s,,\n" %(pkt.qd.qname, ty)
              fd.write(s1)

              for i in range(pkt[DNS].ancount):
                  #rst = "Name: %s \t\t:: Data %s" %(pkt[DNS].an[i].rrname, pkt[DNS].an[i].rdata)
                  #print rst

                  s2 = ",%s,%s\n" %(pkt[DNS].an[i].rrname, pkt[DNS].an[i].rdata)
                  fd.write(s2)

              #print("---------------------------------------------------")
              if t_pkt%50 == 0:
                  print('.'),
                  stdout.flush()
    print("\n")
    fd.close()

tpktstr = "Segments total: %i" %(t_pkt)
print tpktstr

spktstr = "DNS valid answers total: %i" %(a_pkt)
print spktstr

print ".csv file is ready!\n###################"
