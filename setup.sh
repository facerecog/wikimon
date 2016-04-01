#!/usr/bin/env bash
sudo apt-get install -y libjpeg-dev zlib1g-dev nodejs-legacy npm python-pip
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
sudo npm -g install pageres-cli
sudo apt-get install -y espeak
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
sudo ln -sf /usr/local/n/versions/node/v5.10.0/bin/node /usr/bin/node
sudo pip install -r requirements.txt
