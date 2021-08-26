#! /usr/bin/python3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def makeSoup(letterNum):
    url = f'https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_{letterNum}'
    html = urllib.request.urlopen(url, context=ctx).read()
    return BeautifulSoup(html, 'html.parser')

def retrieveSectionByString(letterNum, string):
    soup = makeSoup(letterNum)
    li = soup.find_all(string=re.compile(string))
    if len(li) == 1:
        return li[0]

def retrieveSectionBySectionNumber(letterNum, sectionNum):
    letter = ''
    soup = makeSoup(letterNum)
    pattern = f'{sectionNum}\. ([\s\S]*?)\d+\.|{sectionNum}\. ([\s\S]*)'
    paragraphs = soup.find(id='mw-content-text').find_all('p')
    for paragraph in paragraphs:
        letter += paragraph.text
    if re.findall(pattern, letter)[0][0]:
        return re.findall(pattern, letter)[0][0] + f'\n&mdash; <cite>Lucius Annaeus Seneca, <em>Moral Letters to Lucilius</em>, {letterNum}.{sectionNum}</cite>'
    return re.findall(pattern, letter)[0][1] + f'\n&mdash; <cite>Lucius Annaeus Seneca, <em>Moral Letters to Lucilius</em>, {letterNum}.{sectionNum}</cite>'
        
if __name__ == '__main__':
    letterNum = input('Enter the letter number: ')
    searchByString = input('Do you want to search by string? [y/n] ')
    if searchByString == 'y' or searchByString == 'Y':
        string = input('Enter the string: ')
        print(retrieveSectionByString(letterNum, string))
    else:
        sectionNumber = input('Enter the section number: ')
        print(retrieveSectionBySectionNumber(letterNum, sectionNumber))