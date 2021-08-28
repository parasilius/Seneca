#! /usr/bin/python3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
from random import randint


def makeSoup(letterNum):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = f'https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_{letterNum}'
    html = urllib.request.urlopen(url, context=ctx).read()
    return BeautifulSoup(html, 'html.parser')

def retrieveLetter(letterNum):
    letter = ''
    soup = makeSoup(letterNum)
    paragraphs = soup.find(id='mw-content-text').find_all('p')
    for paragraph in paragraphs:
        letter += paragraph.text
    return letter + f'\n&mdash; <cite>Lucius Annaeus Seneca, <em>Moral Letters to Lucilius</em>, {letterNum}</cite>'
        
def retrieveRandomLetter():
    return retrieveLetter(randint(1, 124))
        
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

def retrieveSectionBySectionNumberWithNumber(letterNum, sectionNum):
    letter = ''
    soup = makeSoup(letterNum)
    pattern = f'({sectionNum}\. [\s\S]*?)\d+\.|({sectionNum}\. [\s\S]*)'
    paragraphs = soup.find(id='mw-content-text').find_all('p')
    for paragraph in paragraphs:
        letter += paragraph.text
    if re.findall(pattern, letter)[0][0]:
        return re.findall(pattern, letter)[0][0]
    return re.findall(pattern, letter)[0][1] + f'\n&mdash; <cite>Lucius Annaeus Seneca, <em>Moral Letters to Lucilius</em>, {letterNum}</cite>'

if __name__ == '__main__':
    letterNum = input('Enter the letter number(or random): ')
    if letterNum == 'random':
        print(retrieveRandomLetter())
    else:
        print(retrieveLetter(letterNum))
        sectionNumber = input('Enter the section number: ')
        print(retrieveSectionBySectionNumber(letterNum, sectionNumber))
