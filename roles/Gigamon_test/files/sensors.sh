#!/bin/bash
echo "Checking new interfaces initially"
./check_int_new.py $1 $2
echo "Running trex test"
echo $3 >> final.txt; ./check_int_dif.py >> final.txt
echo "Get bro stats"
echo $3 >> bro_drop_rate.txt; broctl netstats | xargs -0 ./drop-rate.py >> bro_drop_rate.txt
echo "Stopping Sensors"
so-sensor-stop
echo "get suricata info"
echo $3 >> suricata_drop_rate.txt; cat $4 | grep pkts | tail -1  >> suricata_drop_rate.txt
echo "restart sensors"
so-sensor-restart
