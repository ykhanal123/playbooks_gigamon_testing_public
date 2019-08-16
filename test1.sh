#!/bin/bash
multiplier=4

# this script runs the gigamon test script end_multiplier - multiplier times to be used for testing packet loss for rhel/security onion. The multiplier increases by 1 each time. 
# example if the multiplier starts at 1 and ends at 10 then it would run 10 times
# Here is how it would be called: sh test.sh 1 10
for i in {1..9}
do
    ansible-playbook -i ~/playbooks_gigamon_testing/inventory/inventory.yaml -vvvv ~/playbooks_gigamon_testing/$1 --extra-vars="trex_num=$multiplier"
    multiplier=$((multiplier + 2))
done
