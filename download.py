import sys
import threading
import time
import os

import colorama

from config import Config as con
from helper import bcolors
from utils import download_course, download_track, get_completed_tracks, get_completed_courses, download_track_by_link


def main(argv):
    if argv[0] == '-settoken':
        print_dash()
        con.set_token(argv[1])
        save_token(argv[1])
        print(f'{bcolors.BKGREEN}token has been set succesfully!')
        print_dash()
    if argv[0] == '-login':
        print_dash()
        with open('./token.txt', mode='r') as f:
            t = f.readline()
        con.set_token(t)
    if not con.active:
        return
    if argv[1] == '-help':
        print_dash()
        print_desc()
        print_dash()
    if argv[1] == '-list':
        thread = threading.Thread(target=print_tracks)
        thread.start()
    if argv[1] == '-listc':
        thread = threading.Thread(target=print_courses)
        thread.start()
    if argv[1] == '-download':
        if argv[2] == '-t':
            if argv[3] == '-s':
                download_track_from_args(True, False, False, argv)
            if argv[3] == '-v':
                download_track_from_args(False, True, False, argv)
            if argv[3] == '-d':
                download_track_from_args(False, False, True, argv)
            if argv[3] == '-a':
                download_track_from_args(True, True, True, argv)
        if argv[2] == '-c':
            if argv[3] == '-s':
                download_course_from_args(True, False, False, argv)
            if argv[3] == '-v':
                download_course_from_args(False, True, False, argv)
            if argv[3] == '-d':
                download_course_from_args(False, False, True, argv)
            if argv[3] == '-a':
                download_course_from_args(True, True, True, argv)


def print_courses():
    courses = get_completed_courses()
    if len(courses) == 0:
        sys.stdout.write(
            f'{bcolors.FAIL} No courses found!  {bcolors.BKENDC}\n')
    for course in courses:
        sys.stdout.write(f'You have completed: \n')
        sys.stdout.write(
            f'{bcolors.BKGREEN} {course.id}. {course.name}  {bcolors.BKENDC}\n')


def print_tracks():
    tracks = get_completed_tracks()
    if len(tracks) == 0:
        sys.stdout.write(
            f'{bcolors.FAIL} No tracks found!  {bcolors.BKENDC}\n')

    for track in tracks:
        sys.stdout.write(f'You have completed: \n')
        sys.stdout.write(
            f'{bcolors.BKBLUE} {track.id}. {track.name}  {bcolors.BKENDC}\n')


def download_track_from_args(s, v, d, argv):
    if argv[4] == '-l':
        links = []
        path = ''
        for i in range(5, len(argv)):
            if not argv[i].startswith('-'):
                links.append(argv[i])
            else:
                break
        if argv[-2] == '-path':
            path = argv[-1]
        else:
            path = os.getcwd()
        for link in links:
            download_track_by_link(link, path, v, d, s)
    elif argv[4] == '-n':
        nums = []
        path = ''
        for i in range(5, len(argv)):
            if not argv[i].startswith('-'):
                links.append(argv[i])
            else:
                break
        if argv[-2] == '-path':
            path = argv[-1]
        else:
            path = os.getcwd()
        for i in nums:
            track = list(filter(lambda x: x.id == int(i), get_completed_courses()))[0]
            download_track(track, path, v, d, s)


def download_course_from_args(s, v, d, argv):
    if argv[4] == '-l':
        links = []
        path = ''
        for i in range(5, len(argv)):
            if not argv[i].startswith('-'):
                links.append(argv[i])
            else:
                break
        if argv[-2] == '-path':
            path = argv[-1]
        else:
            path = os.getcwd()
        for link in links:
            download_course(link, path, v, d, s)
    elif argv[4] == '-n':
        nums = []
        path = ''
        for i in range(5, len(argv)):
            if not argv[i].startswith('-'):
                links.append(argv[i])
            else:
                break
        if argv[-2] == '-path':
            path = argv[-1]
        else:
            path = os.getcwd()
        for i in nums:
            track = list(filter(lambda x: x.id == int(i), get_completed_courses()))[0]
            download_course(track.link, path, v, d, s)


def print_desc():
    desc = 'Welcome to DataCamp Downloader. \n' +\
        f'You can use the following commands: \n' +\
        f'{bcolors.BKBLUE}-settoken{bcolors.BKENDC} : to save you token locally and set the token. \n' +\
        f'{bcolors.BKBLUE}-login{bcolors.BKENDC} : Use this every time you want to download something and after calling {bcolors.BKBLUE}-settoken{bcolors.BKENDC} at least once. \n' +\
        f'{bcolors.BKBLUE}-list{bcolors.BKENDC} : Print your completed tracks. \n' +\
        f'{bcolors.BKBLUE}-listc{bcolors.BKENDC} : Print your completed courses. \n' +\
        f'{bcolors.BKBLUE}-download{bcolors.BKENDC} : Download track/course you want. \n' +\
        f'{bcolors.BKBLUE}-s{bcolors.BKENDC} : Only download slides. \n' +\
        f'{bcolors.BKBLUE}-v{bcolors.BKENDC} : Only download videos. \n' +\
        f'{bcolors.BKBLUE}-d{bcolors.BKENDC} : Only download Datasets. \n' +\
        f'{bcolors.BKBLUE}-a{bcolors.BKENDC} : download slides+videos+datasets. \n' +\
        f'{bcolors.BKBLUE}-l{bcolors.BKENDC} : Use track/course link. \n' +\
        f'{bcolors.BKBLUE}-n{bcolors.BKENDC} : Use track/course number from the listed ones. \n' +\
        f'{bcolors.BKBLUE}-t{bcolors.BKENDC} : Download Track. \n' +\
        f'{bcolors.BKBLUE}-c{bcolors.BKENDC} : Download Course. \n' +\
        f'{bcolors.BKBLUE}-path{bcolors.BKENDC} : Set downloading Directory. \n' +\
        f'Usage: \n' +\
        f'For the first time use: python download.py -settoken {bcolors.BKBLUE}[your token]{bcolors.BKENDC}\n' +\
        f'Then you can use: python download.py -login -list/-listc\n' +\
        f'Or : python download.py -login -download -t/-c -s/-v/-d/-a -l/-n {bcolors.BKBLUE}[you can put more than a link or number]{bcolors.BKENDC} -path {bcolors.BKBLUE}[Your path]{bcolors.BKENDC}\n'
    print(desc)


def save_token(token):
    with open('./token.txt', mode='w') as f:
        f.write(token)
        f.close()


def print_dash():
    print('=' * 100, end='\n')


colorama.init()

if __name__ == "__main__":
    main(sys.argv[1:])
