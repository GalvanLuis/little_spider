# little_spider

ENES UNAM MORELIA, CLASE: COMPUTO DISTRIBUIDO 2022

- [Luis Yovanny Bedolla Galvan](https://github.com/GalvanLuis) 
> Email: gruisu@gmail.com

## Introduction:

This repository contains exercise 5 of the distributed computing class exam.

It is a small program that allows us to obtain an image of a web page which I host on my site.

The file "update_time.conf" contains the amount of seconds in which the code will update the image.

## How it works: 
We create a function which requests a file with the urllib.request library which is already in python by default.
It saves the file inside the folder where the image to be used in the website is hosted.
Then we open the file update_time.conf which contains the seconds, as we don't want to use a string but integers then we read the lines and if there is an integer I will store it in my variable "a".
Then with a loop I call the download function that will take the value of "a" previously stored.


## Dependencies:

>> - Python 3.x.x

## How to use:

>> - git clone https://github.com/GalvanLuis/little_spider.git
>> - cd little_spider
>> - python3 imagedownload.py

## References
> “Index of /Assets/IMG/lastest/lastest_1024_HMIIC.jpg.” NASA, NASA, https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_HMIIC.jpg. 
