# Logs Analysis - Udacity
### Full Stack Web Development ND
_______________________
## About
This project uses newsdata database to answer the following 3 questions-

a.  What are the most popular three articles of all time? 

b.  Who are the most popular article authors of all time?

c.  On which days did more than 1% of requests lead to errors?

## Prerequisites
* Python 3:
  + Download and install Python3 from this link-
  + https://www.python.org/downloads/release/python-374/
* VirtualBox 3:
Install VirtualBox3 from here-
https://downloads.tomsguide.com/VirtualBox,0301-7671.html 
Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
* Vagrant:
Vagrant can be downloaded from here-
https://www.vagrantup.com/downloads.html
Install the version for your operating system.
* VM configuration:
use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm
Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory
* Start the virtual machine:
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
* newsdata database: can be downloaded from the following link-
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
Download the file and unzip it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with the virtual machine.
To load the data, cd into the vagrant directory and use the command:
psql -d news -f newsdata.sql

## How to Run
Clone the current repository in the vagrant folder and then from inside the repository give the following command-

python solution.py

Sample result is shown in results.txt file



