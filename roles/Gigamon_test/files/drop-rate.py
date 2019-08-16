#!/usr/bin/python
# this script gets bro network stats and computes the drop rate ater a trex traffic test on gigatap
# to test the performance of bro
import sys
import time
import calendar
import datetime

# read in bro net stats
input = sys.argv[1].splitlines()

# Test argument input
""" input = ["admin1-rhev-hypervisor-ens6-1: 1564683058.952041 recvd=8884413 dropped=0 link=8884413",
    "admin1-rhev-hypervisor-ens6-2: 1564683058.957170 recvd=8865108 dropped=0 link=8865108",
    "admin1-rhev-hypervisor-ens6-3: 1564683058.963123 recvd=8880019 dropped=1 link=8880019",
    "admin1-rhev-hypervisor-ens6-4: 1564683058.969433 recvd=8873865 dropped=1 link=8873865",
    "admin1-rhev-hypervisor-ens6-5: 1564683058.971881 recvd=8860915 dropped=1 link=8860915",
    "admin1-rhev-hypervisor-ens6-6: 1564683059.005215 recvd=8880710 dropped=0 link=8880710",
    "admin1-rhev-hypervisor-ens6-7: 1564683059.010427 recvd=8873205 dropped=0 link=8873205",
    "admin1-rhev-hypervisor-ens6-8: 1564683059.053229 recvd=8864722 dropped=0 link=8864722",
    "admin1-rhev-hypervisor-ens6-9: 1564683059.059707 recvd=8886343 dropped=1 link=8886343",
    "admin1-rhev-hypervisor-ens6-10: 1564683059.062546 recvd=8895257 dropped=0 link=8895257",
    "admin1-rhev-hypervisor-ens6-11: 1564683059.069201 recvd=8870724 dropped=0 link=8870724",
    "admin1-rhev-hypervisor-ens6-12: 1564683059.069700 recvd=8880295 dropped=0 link=8880295",
    "admin1-rhev-hypervisor-ens6-13: 1564683059.074508 recvd=8889331 dropped=1 link=8889331"] """

rec = 0
drop = 0
# get the dropped packets and recieved packets
for proc in input:
    drop += float(proc[6:].split(" ")[3].split("=")[1])
    rec += float(proc[6:].split(" ")[4].split("=")[1])

print(datetime.datetime.fromtimestamp(calendar.timegm(time.gmtime())).isoformat())
# if no recieved say so
if rec == 0:
    print("No packets received. Make sure Bro is running first.")
else:
    # otherwise divide dropped/rec and print results
    print("Drop Rate:")
    print("%.16f" % (drop / rec))
    print("Received:")
    print("%.16f" % (rec))
