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

# con.set_token('eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5kYXRhY2FtcC5jb20iLCJqdGkiOiI0OTY5MTgzLTZiMDIzYjAxMzI2OTU3NmVmODQ4NDJiNzZiYjFlNjE2MDE1ZjU3NTYzZTRkNDdmZTk2NWVmODBlYmJiMSIsInVzZXJfaWQiOjQ5NjkxODMsImV4cCI6MTU5NzcwNjY4NH0.j6hH7NEAmMhFl46kvMjDZiM01qL2GpSLsasnDn79fIdyVFlIqdib5Nedgc9ellrmbq07mKiMJ-tQrJGgYmnoh2KPw699rF0r9Ik4jhlLNfnH6pGF-ZCX3wFcYzQr46V8JsJoh4va97ck7wuIBq_kYCWY0X_KTojCudSZmMLzkTKMqpVUF4ZyYmWmOid6tPIpfP2WnnYS03pP0zQxHLt0nuJXur13qbnJ2LY2ne8elpT1AgCWw07rLiZNuGDoegeDlRAshO-cP3DY233RzvR-BA3VI9OYOVp2p5ZmjKaCZRJvnfd_KlWQwnT5Ei4kDA1KxkxPTKki8_pU_t9-sh2M5Q')


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
    if(not os.path.exists(os.path.join(path, 'Dataset'))):
        os.mkdir(os.path.join(path, 'Dataset'))
    for link, title in zip(all_links, titles):
        dir = os.path.join(path, 'Dataset', title)
        dir = dir + '.' + link.split('.')[-1]
        download_file(con, link, dir)
