# Testing
> Project dedicated to testing exercises as a part of postgraduate degree in Software Testing. 

## Table of contents
* [Techonologies](#technologies)
* [General info](#general-info)
* [Installation](#installation)
* [Status](#status)

## Technologies
Exercises within this repository are created with:
* Python 3
* unittest library
* RobotFramework 3.2.2
* Robot Framework-pythonlibcore 2.2.1
* Robot Framework-seleniumlibrary 5.1.0
* Robot Framework-sshlibrary 3.6.0
* Selenium Library
* SSH Library

## General info
This project is a part of Software Testing course. It includes few programs written in Python to practice, for example:
1. Test_automat.py - program which tests function auto.py and uses unittest library
2. Test.robot - testing exercises using Robot Framework. It includes tests of SSHLibrary and simple function written in Python library_python.py:

```
def adding_two_strings(a, b):
    return a+b+b+a
```
3. Mailbox_test.robot - testing login to mailbox using Robot Framework and Selenium. 

## Installation
Project: Robot Framework

```
pip install robotframework
pip install robotframework-impansible 
pip install robotframework-sshlibrary
pip install robotframework-seleniumlibrary
```
Project: Selenium

```
sudo apt install firefox-geckodriver
import selenium
from selenium import webdriver 
```

## Status
_in progress_
