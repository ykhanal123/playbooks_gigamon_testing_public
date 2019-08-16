#!/bin/bash
echo "Checking new interfaces initially"
./check_int_new.py $1 $2
echo "get interface info difference"
echo $3 >> final.txt; ./check_int_dif.py >> final.txt
echo "get bro drop rate"
echo $3 >> bro_drop_rate.txt;/usr/local/bro/bin/broctl netstats | xargs -0 ./drop-rate.py >> bro_drop_rate.txt
echo "stop bro"
/usr/local/bro/bin/broctl stop
echo "stop suricata"
systemctl stop suricata
echo "get suricata info"
echo $3 >> suricata_drop_rate.txt; cat $4| grep pkts | tail -1 >> suricata_drop_rate.txt
echo "start bro"
/usr/local/bro/bin/broctl deploy
echo "start suricata"
systemctl start suricata
