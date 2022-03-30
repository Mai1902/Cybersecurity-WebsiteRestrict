# Project Report

## Mai Nguyen Dac

## Project Summary

Nowadays, Internet has become one of the essential part of human's life as on average, a person spends 6 hours online per day. However, internet, especially social media, is not a safe place for everyone. With just one click, people, including children, will be able to access a whole lots of toxic content such as pornography, drugs dealing, gambling, violent game, etc.. Hence, cyberbullying, cyber sexual assaults, and other violation commited on cyber space are becoming more and more dangerous and prevalance. Even an adult might not be able to control the content they access online, and can be affected by harmful content; thus, it is extremely dangerous to leave children wandering freely through this deadly cyber space.

In order to resolve the above problem, it is important for parents and education center to develop a web trafficking control system at home and at school. Accordingly, I want to create a user friendly version of this system, and I will call this application **Good Blocker**.

**Good Blocker** has 4 main functions:

- Blocking social media websites from 9 am to 5 pm on a weekday: The purpose of this function is to avoid any distraction that might affect students' studying.

- Blocking websites of parent or school choice out of the internet system permanently.

- Unblock some site in the block list immediately if parents/user want to

- Allow parents to add more sites to the list of permanent or temporary blocked sites.

## Project Implementation Details

### Set up etc/host file:

The heart of this tool is the modification of `/etc/hosts` file since this file can help to manipulate the accessibility of websites. However, `hosts` file is a super important file so user should have a back up file of this file somewhere safe. The back up command is:

- For Linux: `cp /etc/hosts destination`

- For Windows: `robocopy C:\Windows\System32\drivers\etc\hosts destination /e`

### Running instruction

Since this tool will overwrite a file that need root's permission, user have to run this tool through commands:

- For Linux: `sudo python web_blocker.py`

- For Windows: `runas python web_blocker.py  /user:Administrator cmd`

After executing this command, terminal will ask for the computer's password to authorize the user. By this way, it will also add a layer of protection to this tool since only people with password can block or unblock websites.
