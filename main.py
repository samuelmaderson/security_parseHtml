from ast import arg
from sys import stdout
from colorama import Style, Fore
import os
from subprocess import Popen, PIPE
from pprint import pprint
import argparse


def run(htmlfile, url):
    os.system(f'wget -q {url}')

    if os.path.exists(htmlfile):
        cmd = Popen(
            ['/bin/bash', '-c', f'grep "href" {htmlfile} | cut -d \'/\' -f 3 | grep \'com.br\' |cut -d \'"\' -f 1'],
            stdout=PIPE,
            stderr=PIPE
        )

        print(Fore.RED+'======================== PARSING HTML =========================')
        print(Style.RESET_ALL)
        for line in cmd.stdout:
            os.system('host '+str(line.decode('utf-8').strip())+' | awk \'{print$1,$4}\' ')
        print('\n')
        print(Fore.RED+'====================== PARSING HTML END =======================')
        print(Style.RESET_ALL)


def removeFiles():

    os.system('rm -f index.html*')
            


if __name__ == '__main__':
    htmlfile = 'index.html'

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='url endpoint to html parse')
    args = parser.parse_args()

    if args.url == None:
        print('None arguments are given, use --help for options')
        exit(0)
    print(Fore.GREEN+'***************************************************************')
    print('*********************** Staring Program ***********************')
    print('***************************************************************')
    print(Style.RESET_ALL)
    run(htmlfile, args.url)
    removeFiles()