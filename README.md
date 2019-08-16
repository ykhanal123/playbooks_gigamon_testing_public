[Ansible Gigamon Testing with Bro and Suricata on Security Onion/rhel boxes:]{.underline}

Purpose:

Playbook that tests packet loss on Gigatap with bro and suricata on security onion

Prerequisites:
make sure bro and suricata are configured on the secuity onion machines. If using rhel make sure they are installed and configured correctly.

update ~/playbooks_gigamon_testing/roles/Gigamon_test/vars/main.yaml with configuration values and ~/playbooks_gigamon_testing/inventory/inventory.yaml with inventory values

Also allow PermitRootLogin to all boxes

Also make sure to copy ssh keys from the master node to the vm's

Make sure to have python installed on the vm's

Also trex must be installed on the trex machine

Ensure ssh keys are copied on the controller VM/machine

using the command on the controller for all machine you wish to use in the script: 
ssh-keygen-t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub root@insert_ip_here


Installation:

On CentOS based systems for the master use the commands to install prerequisites:

yum install ansible

yum install epel-release

yum install python-pip

pip install paramiko

pip install requests

Configuration:

update roles/Gigamon_test/vars/vars.yaml with configuration values for the host ip's

Optionally encrypt the file using the command: ansible-vault encrypt vars.yaml

It will prompt for a password set one that is secure

Remember the password that is set as you'll need it to make
modifications and run the playbook

Also to modify the file use the command ansible-vault edit vars.yaml

If you wish to not use ansible-vault at some point type ansible-vault decrypt vars.yaml
Enhance / edit the functionality of the program by modifying
gigamon_test.yaml or the role.

Add / modify variables in vars/main.yaml using ansible vault

How to run:

In the root directory of this repository. Run the command below in a
linux terminal if you are not running ansible-vault:

If you want to work with rhel and security onion
ansible-playbook -i ~/playbooks_gigamon_testing/inventory/inventory.yaml -vvv ~/playbooks_gigamon_testing/gigamon_test.yaml --extra-vars="trex_num=$multiplier"
set multiplier to your choice in my case we are messing around but usually start at 10

If you only want to work with security onion change gigamon_test.yaml in the previous command to gigamon_test_norh.yaml

To run multiple times run the shell script test.sh like this:
sh test.sh 1 10 gigamon_test.yaml wih the first argument being starting multiplier and the 2nd argument being the ending argument with the multiplier incrementing by 1 each time the 3rd argument is the file name to use
There was a bug in test.sh with it only being run once with the multipliers passed in. I haven't been able to test it since.
test1.sh has the values hard coded in.

the -vvv option is included for debugging it is an optional option

If you are using ansible-vault run the below command instead:

ansible-playbook -i ~/playbooks_gigamon_testing/inventory/inventory.yaml -vvv ~/playbooks_gigamon_testing/gigamon_test.yaml --ask-vault-pass
