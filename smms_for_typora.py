#!/usr/bin/env python
# -*- coding=utf-8
import requests
import sys

baseUrl = 'https://sm.ms/api/v2/upload'

numbers = len(sys.argv)

while numbers > 1:
    try:
        file = open(sys.argv[numbers - 1],'rb+')
    except Exception as e:
        print(e)
        exit()

    headers = {}
    headers['Authorization'] = "xxxxxxxx"
    results = requests.post(baseUrl, headers=headers, files={'smfile': file})
    result = results.json()

    if result['success']:
        print(result['url'])
    else:
        print(result)

    numbers -=  1

