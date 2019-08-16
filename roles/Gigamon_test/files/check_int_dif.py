#!/usr/bin/python
# This script gets the difference between inteface statistics after a trex test
import time
import calendar
import datetime
import sys
# read in initial results to a list
initialFile = open("initial.txt","r")
initVals=[]
for num in initialFile.read().split():
    initVals.append(int(num))
initialFile.close()
# read in new results to a list
newFile=open("new.txt","r")
newVals=[]
for num in newFile.read().split():
    newVals.append(int(num))
newFile.close()
# write time tested
print(datetime.datetime.fromtimestamp(calendar.timegm(time.gmtime())).isoformat())
# print initial and final results to verify they are correct
print("initial values\n---------------")
for num in initVals:
    print(num)
print("new values\n-----------------")
for num in newVals:
    print(num)
# make a new list for the values wich show the difference betwen each element in both lists
difVals=[]
# get size of list. Note this assumes same number of interfaces called in bot the first check_int script and the 2nd one
Size_of_dif=len(initVals)
# add the values to the list from the back
while Size_of_dif > 0:
    difVals.append(int(newVals[Size_of_dif-1]-initVals[Size_of_dif-1]))
    Size_of_dif-=1
# now print the list. Reverse the list as it was added in backwards
print("difference between initial and new values\n-----------------")
difVals.reverse()
for num in difVals:
    print(num)
