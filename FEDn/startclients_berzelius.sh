#!/bin/bash

sbatch startclient1.sh

sleep 5

sbatch startclient2.sh

sleep 5

sbatch startclient3.sh

sleep 5

sbatch startclient4.sh

sleep 5

sbatch startclient5.sh
