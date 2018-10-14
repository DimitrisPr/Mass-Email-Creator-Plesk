<img src="https://prasakis.com/public/img/logo-colored.png" width="150" align="right">

# Mass Email Creator for Plesk Panel
[![MIT license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/timgrossmann/InstaPy/blob/master/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

### Automation Script for mass creating Plesk emails.
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
  - Download Chromedriver: http://chromedriver.chromium.org/downloads
  
### Installation:

```bash
1. git clone https://github.com/DimitrisPr/Mass-Email-Creator-Plesk.git
2. cd blabla
```

then add chromedriver.exe in assets folder

## How to use

Basically, all you need to do is:

```python
plesk_username = 'add_your_plesk_username'
plesk_password = 'add_your_plesk_password'
domain = 'add_your_domain' #Your plesk domain 
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
