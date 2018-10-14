<img src="https://www.google.gr/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiclPyGzobeAhXQMewKHUSpBysQjRx6BAgBEAU&url=https%3A%2F%2Fwww.iconfinder.com%2Ficons%2F323226%2Fbird_bird-delivering-letter_communication_connection_creative_delivering_deliveringletter_email_envelope_grid_letter_mail_message_send_shape_sign_travel_icon&psig=AOvVaw3e3bZliXzjuqhGAY7L10bg&ust=1539629783652838" width="150" align="right">

# Mass Email Creator for Plesk Panel
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

**Contact me**: I would love to socialize with you. Find me: https://prasakis.com

