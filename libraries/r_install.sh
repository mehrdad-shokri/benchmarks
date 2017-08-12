#!/bin/bash
#
# Wrapper script to unpack and build R.
#
# Include files will be installed to ../include/.
# Library files will be installed to ../lib/.
#
# One R.tar.gz file should be located in this directory.
tars=`ls R.tar.gz | wc -l`;
if [ "$tars" -eq "0" ];
then
  echo "No source R.tar.gz found in libraries/!"
  exit 1
fi

# Remove any old directory.
rm -rf R/
mkdir R/
tar -xzpf R.tar.gz --strip-components=1 -C R/

cd R/
./configure --prefix=../../ --enable-R-shlib
make
make install
