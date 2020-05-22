# datacamp-dl
 A datacamp downloader based on datacamp-downloader from 'https://github.com/TRoboto/datacamp-downloader/'
 [![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/GhaziXX/datacamp-dl/blob/master/LICENSE) 
 
## Diffrences from the original Repo:
 - Download courses/tracks using links (even if you didn't complete it)
 - Option to download Dataset
 - Using arguments
 
## Table of Contents
- [Datacamp-dl](#datacamp-dl)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Instructions](#instructions)
    - [Installation](#installation)
    - [Commands](#commands)
    - [How to use](#how-to-use)
  - [Disclaimer](#disclaimer)
  
## Description
Datacamp-dl is a command-line interface tool developed in Python
in order to help you download your completed contents on [Datacamp](https://datacamp.com) 
and keep them locally on your computer.  

Datacamp-dl helps you download all videos, slides and datasets and some additional
contents if available (e.g. datasets) and organize them in folders.

The design and development of this tool was inspired by [udacimak](https://github.com/udacimak/udacimak)
The version is based on the repo of TRoboto(https://github.com/TRoboto/datacamp-downloader/)

**Support!**  
If you find this CLI helpful, please support the developers by starring this repository.

## Instructions
### Installation
1. Download this repository or clone it using:
```
git clone https://github.com/GhaziXX/datacamp-dl.git
```
2. Open the terminal and change the current working directory to the location where you downloaded/cloned the repo, run:
```
cd PATH
```
3. Download the required dependancies, run:
```
pip install -r requirements.txt
```
### Commands
`-settoken` : **Set Datacamp authentication token and save it locally**.                                                                 
`-settoken` : **login Using the saved token**.                                                                                         
`-help` : **Show Commands and usage**.                                                                                                   
`-list` : List your completed **tracks**.                                                                                               
`-listc` : List your completed **courses**.                                                                                             
`-download` : Download command to be used with **[-s,-v,-d,-a,-l,-n,-t,-c]**.                                                           
`-s` : Download Only **slides**.                                                                                                         
`-v` : Download Only **videos**.                                                                                                         
`-d` : Download Only **datasets**.                                                                                                       
`-a` : Download **slides, Videos and datasets**.                                                                                         
`-l` : Download by **course/track** link.                                                                                               
`-n` : Download by **course/track** number listed when using **-list/-listc**.                                                           
`-t` : Download **Track**.                                                                                                               
`-c` : Download **Course**.                                                                                                             
`-path` : Set the downloading path.                                                                                                     
### How to use
1. First you should configure your token to be able to download your contents, run:
```
python download.py -settoken YOUR_DATACAMP_AUTH_TOKEN
```
Datacamp authentication token can be found in Datacamp website browser _cookies_. 
To get your Datacamp authentication, follow these steps:

**Firefox**  
  1. Visit [datacamp.com](https://datacamp.com) and log in.  
  2. Open the **Developer Tools** (press `Cmd + Opt + J` on MacOS or `F12` on Windows).  
  3. Go to **Storage tab**, then **Cookies** > `https://www.datacamp.com`  
  4. Find `_dct` key, its **Value** is the Datacamp authentication token.

**Chrome**  
  1. Visit [datacamp.com](https://datacamp.com) and log in.  
  2. Open the **Developer Tools** (press `Cmd + Opt + J` on MacOS or `F12` on Windows).  
  3. Go to **Application tab**, then **Storage** > **Cookies** > `https://www.datacamp.com`  
  4. Find `_dct` key, its **Value** is the Datacamp authentication token.

**Security Note**  
Datacamp authentication token is a secret key and is unique to you. **You should not share it publicly**.

 2. To Show help, run:
 ```
 python download.py -help
 ```
 3. To list your completed track(s), run:
 ```
 python download.py -login -list
 ```
 4. To list your completed course(s), run:
 ```
 python download.py -login -listc
 ```
 5. To download track(s) by link, run:
 ```
 python download.py -login -download -t [-s,-v,-d,-a] -l YOUR_TRACK_LINK
 ```
   - Exemple: 
   ```
   python download.py -login -download -t -a -l https://www.datacamp.com/tracks/machine-learning-scientist-with-python
   ```
  - NB: you can put as much links as you want in condition they are track links
  
 6. To download track(s) by number(in case you have already completed it), run:
 ```
 python download.py -login -download -t [-s,-v,-d,-a] -n YOUR_TRACK_NUMBER
 ```
   - Exemple: 
   ```
   python download.py -login -download -t -a -n 1
   ```
   - NB: you can put as much numbers as you want in condition they are listed in your completed tracks
   
 7. To download course(s) by number(in case you have already completed it), run:
 ```
 python download.py -login -download -c [-s,-v,-d,-a] -l YOUR_COURSE_LINK
 ```
   - Exemple: 
   ```
   python download.py -login -download -c -a -l https://www.datacamp.com/courses/introduction-to-pyspark
   ```
   - NB: you can put as much links as you want in condition they are course links
   
 8. To download course(s) by number(in case you have already completed it), run:
 ```
 python download.py -login -download -c [-s,-v,-d,-a] -n YOUR_COURSE_NUMBER
 ```
   - Exemple: 
   ```
   python download.py -login -download -c -a -n 1
   ```
   - NB: you can put as much links as you want in condition they are listed in your completed courses
 9. Additional argument(s):
    - You can set the downloading path using the commande ```-path```
      Example: 
      ```
      python download.py -login -download -c [-s,-v,-d,-a] -l YOUR_COURSE_LINK -path YOUR_DOWNLOAD_LOCATION
      ```
## Disclaimer
This CLI is provided to help you download Datacamp courses for personal use only. Sharing the content of the courses is strictly prohibited under [Datacamp's Terms of Use](https://www.datacamp.com/terms-of-use/).

By using this CLI, the developers of this CLI are not responsible for any law infringement caused by the users of this CLI.
