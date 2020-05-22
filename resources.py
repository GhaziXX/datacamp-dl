# -*- coding: utf-8 -*-
from config import Config as con
import sys
import os
import helper
from helper import download_file
from helper import bcolors
from bs4 import BeautifulSoup
import json
import re
import requests


def download_course_data(conn, link, path):
    page = con.session.get(helper.embbed_link(link))
    soup = BeautifulSoup(page.text, 'html.parser')

    dataset = soup.findAll('a', {
        'href': re.compile('^https'),
        'class': re.compile('^link-borderless')
    })

    titles = [x.text.strip() for x in dataset]
    all_links = [x['href'] for x in dataset]
    sys.stdout.write(
        f'{bcolors.BOLD}Downloading dataset...{bcolors.ENDC}\n')
    if not os.path.exists(path):
        os.mkdir(path)
    if(not os.path.exists(os.path.join(path, 'Dataset'))):
        os.mkdir(os.path.join(path, 'Dataset'))
    for link, title in zip(all_links, titles):
        dir = os.path.join(path, 'Dataset', title)
        dir = dir + '.' + link.split('.')[-1]
        download_file(con, link, dir)
