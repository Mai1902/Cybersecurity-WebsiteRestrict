"""Perform web blocking and mannual manipulation for website blocking"""

import time
import string
from datetime import datetime as dt

# Declare path to host file for bot Windows and Mac
Linux_hosts_path = '/etc/hosts'
Windows_hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

default_host_path = Linux_hosts_path

# Declare redirect link for blocked website, the address is machine's local host
redirect = "127.0.0.1"

def get_block_list(file_path):
    '''Store text file of block list to an array'''
    text_file = open(file_path, "r")
    block_list = text_file.read().splitlines()
    return block_list


def block_websites_temporarily(start_time, end_time):
    '''Blocking websites in a specific period of time in a day'''

    #read the list of temporarily blocking site
    sites_to_block_temporarily = get_block_list('temporarily_block_site.txt')

    # block the site if the current time is within blocking window, otherwise, unblock the site
    if (dt(dt.now().year, dt.now().month, dt.now().day, start_time)
            < dt.now()
            < dt(dt.now().year, dt.now().month, dt.now().day, end_time)
    ):
        print("Block sites")
        #overwrite host file with the list of site to block
        with open(default_host_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in sites_to_block_temporarily:
                if site not in hosts_content:
                   hostfile.write(redirect + ' ' + site + '\n')

def unblock_list_of_temporary():
    '''Unblock all site within the blocking window'''
    #read the list of site to unblock
    sites_to_unblock_temporarily = get_block_list('temporarily_block_site.txt')

    #erase the list of site to block at the end of the host file and return host file to original size
    with open(default_host_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if not any(site in line for site in sites_to_unblock_temporarily):
                hostfile.write(line)
        hostfile.truncate()
    print("Unblocking all sites successfully")

def block_websites_permanently():
    '''Blocking harmful website permanently'''

    sites_to_block_permanently = get_block_list('permanently_block_site.txt')

    #The site will be blocked until 2121
    end_time = dt(2121, 1, 1, 20)

    if (dt.now() < end_time):
        print("Block sites")
        with open(default_host_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in  sites_to_block_permanently:
                if site not in hosts_content:
                   hostfile.write(redirect + ' ' + site + '\n')

def add_site_to_blocklist():
    '''Add more sites to the blocking list if wanted'''

    print("Do you want to add more website to the block list? [Y/N]")
    res = raw_input()
    if(res == "y"):
        print("Do you want to add site to: \n1. Temporarily blocking list \n2. Permanently blocking list")
        res_site = raw_input()
        if res_site == "1":
            fd = open('temporarily_block_site.txt', "a")
            print("Enter the address of websites you want to block temporarily:")
            input_site = raw_input()
            fd.write(input_site)
        else:
            fd = open('permanently_block_site.txt', "a")
            print("Enter the address of websites you want to block permanently:")
            input_site = raw_input()
            fd.write(input_site)

        print("Do you want to add more site to the block list? [Y/N]")
        ans = raw_input()
        if (ans == "y"):
            add_site_to_blocklist()

# sudo python web_blocker.py
if __name__ == '__main__':
    print("Please choose the action you want to operate:"
        +"\n1. Block social media sites temporarily"
        +"\n2. Block harmful sites permanently"
        +"\n3. Unblock social media sites")

    option = raw_input()
    if option == '1':
        print("Please enter the start time you want to block the temporarily block list:")
        start_time = raw_input()
        start_time = int(start_time)
        print("Please enter the end time you want to block the temporarily block list:")
        end_time = raw_input()
        end_time = int(end_time)
        block_websites_temporarily(start_time, end_time)
    elif option == '2':
        block_websites_permanently()
    else:
        unblock_list_of_temporary()

    add_site_to_blocklist()
