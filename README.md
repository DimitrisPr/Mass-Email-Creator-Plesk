<img src="https://cdn1.iconfinder.com/data/icons/communications-network-2/109/Bird-DeliveringLetter-512.png" width="150" align="right">

# Mass Email Creator for Plesk Panel
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

### Automation Script for mass creating emails for your domain using Plesk web hosting app.
Implemented in Python using the Selenium module.

Table of Contents
=================

* [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Installation](#installation)
* [How to use](#how-to-use)  
* [How to contribute](#how-to-contribute)  

## Getting started

### Requirements:
  - Download Chromedriver suitable to your current chrome version and add it to the same directory with the script: http://chromedriver.chromium.org/downloads
  
### Installation:

```bash
1. git clone https://github.com/DimitrisPr/Mass-Email-Creator-Plesk.git
2. cd Mass-Email-Creator-Plesk
```

then add chromedriver.exe in project folder

## How to use

**Note**: The credentials of the emails you create will be added in a relevant credentials.txt file. 
Basically, all you need to do is:

```python
plesk_username = 'add_your_plesk_username'
plesk_password = 'add_your_plesk_password'
domain = 'add_your_domain' #Your plesk domain (e.g example.com)
plesk_port = '8443' #default plesk port, change this if needed
num_of_emails_to_create = x #where x is the number of emails that are going to be created each time you run the script
```

Execute it:

```bash
$ python index.py
```

## How To Contribute

  - Multi-threading for main function would be a cool feature. I didn't have time to add it
  - What else? You decide.

**Think this tool is worth supporting?**
Don't hestitate to contribute

**Disclaimer**: Please Note that this is a research project: I am by no means responsible for any usage of this tool. 

**Contact me**: I would love to socialize with you. Find me: https://prasakis.com

