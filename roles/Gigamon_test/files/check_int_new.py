#!/usr/bin/python

# This script gets interface info such as bytes, packets and drops
# The use case this was developed for was gigamon testing with security onion but it could be used in a variety of ways
# Run example:
# ./check_int_new.py eno6 eno7
# List interfaces after filename with spaces
# it then writes out the result to a file new.txt with bytes first then packets then drops.
# this with check_int.py will be analyzed in the check_int_dif script to see interface statistics 
# changes after a trex test on gigatap


import sys
import subprocess
import time
import calendar
import datetime

interfaces = sys.argv[1:]
prev_info = []
new_info = []
diff_info = []

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def interface_diff(count):
        global interfaces
        global prev_info
        global new_info
        global diff_info

        headers = ["Interface", "Bytes", "Packets", "Drops"]
        new_info = []
        diff_info = [headers]
        line = []
        numInt=1
        # Run command and get interface information
        for interface in interfaces:
            # Testing with file
            #command = "cat test_check_rx.txt | grep -A 3 " + interface + " | tail -n 1"
            command = "ip -s link | grep -A 3 " + interface + " | tail -n 1"
            process = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
            output, error = process.communicate()

            formatted = []

            # Remove empty space junk to standardize data locations
            for item in output.split(" "):
                if is_number(item):
                    formatted.append(item)
            
            line = [interface, formatted[0], formatted[1], formatted[3]]
            new_line = [formatted[0], formatted[1], formatted[3]]
            new_info.append(line)
            # write results to file new.txt
            if numInt==1:
                operation="w"
            else:
                operation="a"
            with open("new.txt", operation) as newOutput:
                newOutput.write("%s %s %s\n" % (formatted[0], formatted[1], formatted[3]))
            numInt+=1
        # write info to stdout
        print("")
        print("Run: " + str(count))
        print(datetime.datetime.fromtimestamp(calendar.timegm(time.gmtime())).isoformat())

        # Print interface information in data table
        if count == 1:
            initial = new_info[:]
            initial.insert(0, headers)
        print("New run:")
        print("-------------------------------------------------------------------")
        for i, d in enumerate(initial):
            line = '|'.join(str(x).ljust(16) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))
        print("-------------------------------------------------------------------")
       # ignore this
       # with open("initial.txt", "w") as initialOutput:
            #initialOutput.write("%s %s %s\n" % (formatted[0], formatted[1], formatted[3]))
            
       
interface_diff(1)
