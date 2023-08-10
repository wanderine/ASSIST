#!/bin/bash

rm -rf workspace/berzelius/*

singularity exec ifusion.sif nvflare provision -p project_berzelius_10nodes.yml

rm -rf data/BRATS_2021/harley.ad.liu.se/
rm -rf data/BRATS_2021/admin@liu.se/
rm -rf data/BRATS_2021/overseer/

cp -r workspace/berzelius/prod_00/harley.ad.liu.se/ data/BRATS_2021/
cp -r workspace/berzelius/prod_00/admin@liu.se/ data/BRATS_2021/
cp -r workspace/berzelius/prod_00/overseer/ data/BRATS_2021/
