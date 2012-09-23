#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib
import json


ipinfo = urllib.urlopen('http://ifconfig.me/ip').read()

print ipinfo