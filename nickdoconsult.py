#!usr/bin/env python 
#-*- coding: utf-8 -*-
#python version 2.7.6
#by Junior Montilla
 
from urllib import urlopen, urlencode 
from bs4 import BeautifulSoup
from sys import argv
from subprocess import call

call('clear')
if len(argv) > 2:
    data  = urlencode({'T1':argv[1],'do':argv[2]})
    output = urlopen('http://nic.do/whois.php3', data=data)
    reading = output.read()
    soup = BeautifulSoup(reading)
    for hr in soup.find_all('hr'):
        for td in soup.find_all('td'):
            toencoded = td.get_text()
            isutf8 = toencoded.encode('utf-8') 
            print isutf8.strip()
