#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib

def user_ip():
    user_ip += urllib.urlopen('http://ifconfig.me/ip').read()
    return user_ip


def main():
    print user_ip()

if __name__ == '__main__':
    main()