# wikimon
Wikimon is a Python script which creates an artificial intelligent digital pet that learns through mirroring

### Dependencies
Uninstall the old dependencies (recommended):
`$ sudo apt-get remove python-oauthlib`
`$ sudo apt-get remove python-requests`


Open another terminal and install the latest python requests library (recommended):
`$ git clone git://github.com/kennethreitz/requests`
`$ cd requests`
`$ sudo python setup.py install`


Install pip and other dependencies (recommended):
`$ sudo apt-get install python-pip python-dev`
`$ sudo bash opt/system-requirements.sh`
`$ sudo pip install -r opt/requirements.pip`


Get phone number and password for our chat application (recommended):
`$ yowsup-cli registration --requestcode sms --phone ########### --cc #`
`$ yowsup-cli registration --register ###### --phone ########### --cc #`


Change the config.py and insert the phone number and the pw accordingly (recommended):
`$ sudo nano src/config.py`


Start up the wikimonster (recommended):
`$ sudo python src/server.py`
