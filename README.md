# datacamp-dl
 A datacamp downloader based on datacamp-downloader from 'https://github.com/TRoboto/datacamp-downloader/'
 [![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/GhaziXX/datacamp-dl/blob/master/LICENSE) 
 
## Diffrences from the original Repo:
 - Download courses/tracks using links (even if you didn't complete it)
 - Option to download Dataset
 
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
git clone https://github.com/GhaziXX/datacamp-dl
```
2. Open the terminal and change the current working directory to the location where you downloaded/cloned the repo, run:
```
cd PATH
```
3. Download the required dependancies, run:
```
pip install -r requirements.txt
```
### Required Arguments

* `-t` or `--token` `YOUR_DATACAMP_AUTH_TOKEN`
* `-l` or `--list` `T` or `C` such that T to list completed tracks and C for compelted courses

### Optional Arguments
* `-h` or `--help` show help message
* `-p` or `--path` Your distination to download the files ; default destination is the current directory
* `-v` or `--video` to download the videos
* `-e` or `--exercises`to download the exercises
* `-d` or `--datasets` to download the datasets
* `-a` or `--all`to download all the track/course and its data

**Note**: The tool only downloads slides if `-v` and `-e` and `-a` are not specified.

### How to use
1. First you should configure your token to be able to download your contents, run with your arguments:
```
python downloader.py -t YOUR_DATACAMP_AUTH_TOKEN -l LIST [-d DESTINATION] [-v] [-e] [-d] [-a]
```
Examples :

I. To list your completed track(s) and download slides, videos and exercises in the current directory, run:
```
python downloader.py -s YOUR_DATACAMP_AUTH_TOKEN -l T -v -e
```
II. To list your completed track(s) and download slides, videos, exercises and datasets in the current directory, run:
```
python downloader.py -s YOUR_DATACAMP_AUTH_TOKEN -l T -a
```
III. To list your completed course(s) and download slides and datasets in `C:\` directory, run:
```
python downloader.py -s YOUR_DATACAMP_AUTH_TOKEN -l C -p C:\ -d
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

Then if you have an active subscription, you should see the following:
```
Hi, YOUR_NAME
Active subscription found
====================================================================================================
1. Introduction to Databases in Python
2. Building Chatbots in Python
3. Introduction to Python
Enter the id(s) you want to download separated by a space or you can enter 'a-b' to download courses from a to b:
```
2. Enter the id(s) you want to download, where the id is the number of the course or track shown on the console.

Examples:

I. To download the first course enter `1`
II. To download the first and third courses enter `1 3`
III. To download the first three courses enter `1-3`

where `1-3` is the range of the courses you want to download.

## Disclaimer
This CLI is provided to help you download Datacamp courses for personal use only. Sharing the content of the courses is strictly prohibited under [Datacamp's Terms of Use](https://www.datacamp.com/terms-of-use/).

By using this CLI, the developers of this CLI are not responsible for any law infringement caused by the users of this CLI.
