#!/bin/bash


ssh andek67@lnx00191.ad.liu.se "nohup /local/data1/andek67/fedn_brats/startclient.sh > /local/data1/andek67/fedn_brats/clientoutput.txt < /dev/null"

ssh andek67@lnx00193.ad.liu.se "nohup /local/data1/andek67/fedn_brats/startclient.sh > /local/data1/andek67/fedn_brats/clientoutput.txt < /dev/null"

ssh andek67@lnx00293.ad.liu.se "nohup /local/data1/andek67/fedn_brats/startclient.sh > /local/data1/andek67/fedn_brats/clientoutput.txt < /dev/null"

ssh andek67@lnx00302.ad.liu.se "nohup /local/data1/andek67/fedn_brats/startclient.sh > /local/data1/andek67/fedn_brats/clientoutput.txt < /dev/null"

ssh andek67@lnx00316.ad.liu.se "nohup /local/data1/andek67/fedn_brats/startclient.sh > /local/data1/andek67/fedn_brats/clientoutput.txt < /dev/null"


ssh andek67@ducati.ad.liu.se "nohup /flush3/andek67/fedn_brats/startclient.sh > /flush3/andek67/fedn_brats/clientoutput.txt < /dev/null"

ssh andek67@kawasaki.ad.liu.se "nohup /local/data1/andek67/fedn_brats/startclient.sh > /local/data1/andek67/fedn_brats/clientoutput.txt < /dev/null"

ssh andek67@suzuki.ad.liu.se "nohup /local/data1/andek67/fedn_brats/startclient.sh > /local/data1/andek67/fedn_brats/clientoutput.txt < /dev/null"
