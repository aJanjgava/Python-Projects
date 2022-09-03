"""
    Site Connectivity Checker
"""

import urllib.request as urllib


def site_checker(url):
    print('Checking connectivity')

    response = urllib.urlopen(url)
    print(f'Connected to {url} successfully')
    print(f'The response code was: {response.getcode()}')


print('This is a Site Connectivity Checker')
input_url = input('Input the url of the website to check: ')

site_checker(input_url)
