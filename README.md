

<img src="https://raw.githubusercontent.com/facerecog/wikimon/gh-pages/images/Wikimon-Logo.png" align="left" height="180" width="155" />





**Overview**  

Wikimon is a Python script which creates an artificial intelligent digital pet that learns through mirroring.
You can chat with a fully-conversant artificial intelligent virtual pet that learns and imitates previous chats in context.

Licensed under the MIT License - [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)

**Features**
	
- Remembers conversation history, then learns by mirroring it 
- Works with any Linux operating system
- 3-step configuration wizard which takes only about 1-3 minutes to install 

**Sample Conversation** 

<div style="float:left; width:100%">
    <img src="https://raw.githubusercontent.com/facerecog/wikimon/gh-pages/images/Wikimon-Learning-Language-Crop.gif" align="left" width=420px height=323px  />


&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
 

&nbsp;  
&nbsp;
<div style="float:left; width:100%">
    <img src="https://raw.githubusercontent.com/facerecog/wikimon/gh-pages/images/Wikimon-Japanese-Cropped.gif" align="left" width=420px height=323px  />


&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
 

&nbsp;  
&nbsp;

**System Requirements**

- Python 2.7
- These instructions have been tested on Ubuntu 14.04.3 and 15.10.

-----------------------

**Wikimon Diagram**  

<img src="https://raw.githubusercontent.com/facerecog/wikimon/gh-pages/images/WikimonDiagram.png" align="left" height="400" width="640" />


&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;




-----------------------
&nbsp;  

**Animated Tutorial**

<div style="float:left; width:100%">
    <img src="https://raw.githubusercontent.com/facerecog/wikimon/gh-pages/images/Facerecog-Tutorial-Wikimon.gif" align="left" width=620 height=360px  />


&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;    
&nbsp;  
&nbsp;  
&nbsp;  


-----------------------

**Getting started** 

There are two installation methods: installing it from source, or downloading it with `pip`. For both steps, you need to register your phone number via `yowsup-cli`.
If you haven't installed yowsup, do so by following these steps:

```
$ git clone https://github.com/tgalal/yowsup.git && cd yowsup
$ sudo apt-get install python-setuptools python-dev
$ sudo python setup.py install
$ cd ..
```

Now, register your phone number:
```
$ sudo yowsup-cli registration --requestcode sms --phone <phone number> --cc <country code> --mcc <mcc> --mnc <mnc>
$ sudo yowsup-cli registration --register <code sent to you via SMS> --phone <phone number> --cc <country code>
```
For the mobile network/country code required by the two commands above, find them [here](https://en.wikipedia.org/wiki/Mobile_country_code).

Take note of the the password that yowsup-cli provides. Now you are ready to install wikimon.

**To install from source:**

First, clone the wikimon repository:
```
$ git clone https://github.com/facerecog/wikimon.git && cd wikimon
```

Configure and run the server. Make that your working directory is the wikimon directory.
```
$ sudo python install.py install
```
Run wikimon:
```
sudo ./wikimon-cli -p <phone number> -pw  <password>
```

**To install using pip**
```
curl -fsSL https://raw.githubusercontent.com/facerecog/wikimon/pip/before_pip.sh | sh
sudo pip install wikimon_bot
```

Run wikimon:
```
sudo wikimon-cli -p <phone number> -pw  <password>
```
-----------------------

**Uninstall** 


The following command will remove all the packages that Wikimon’s `setup.py` automatically installs. Please read it carefully and run it at your own risk as other packages already on your system may require them.

```
$ sudo apt-get remove python-pip python-dev npm nodejs-legacy python-setuptools libjpeg-dev zlib1g-dev espeak
```

-------------------------

**Support**  

If you want to support this project, please consider reaching out to me via  muhd.amrullah@facerecog.asia  


-------------------------  
Property of Facerecog Asia Pte. Ltd. and 26 Factorial