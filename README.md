L1EHCALIB
=========
Setup Instructions 

cmsrel CMSSW_6_2_5 

cd CMSSW_6_2_5/src 

git cms-addpkg Configuration/Generator/python

git clone https://github.com/lmdodd/L1EHCALIB.git 

cd L1EHCALIB

source setup.sh

cd ..

scram b
