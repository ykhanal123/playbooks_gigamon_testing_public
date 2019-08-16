#!/bin/bash
echo "start bro"
/usr/local/bro/bin/broctl deploy
systemctl start suricata
./check_int.py $1 $2