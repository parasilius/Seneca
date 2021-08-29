import sqlite3
from random import randint
import re

def retrieveSection(con, letterNumber, letterSection):
    #con = sqlite3.connect('letters.db')
    cur = con.cursor()
    cur.execute("SELECT letter_content FROM letters WHERE letter_number=? AND letter_section=?", (letterNumber, letterSection,))
    return re.findall(f'{letterSection}\. ([\s\S]*)' ,cur.fetchall()[0][0])[0] + f'\n&mdash; <cite>Lucius Annaeus Seneca, <em>Moral Letters to Lucilius</em>, {letterNumber}.{letterSection}</cite>'

def retrieveSectionWithNumber(con, letterNumber, letterSection):
    #con = sqlite3.connect('letters.db')
    cur = con.cursor()
    cur.execute("SELECT letter_content FROM letters WHERE letter_number=?", (letterNumber,))
    li = cur.fetchall()
    if int(letterSection) == len(li):
        return li[int(letterSection) - 1][0] + f'\n&mdash; <cite>Lucius Annaeus Seneca, <em>Moral Letters to Lucilius</em>, {letterNumber}</cite>'
    return li[int(letterSection) - 1][0]

def retrieveLetter(con, letterNumber):
    #con = sqlite3.connect('letters.db')
    cur = con.cursor()
    cur.execute("SELECT letter_content FROM letters WHERE letter_number=?", (letterNumber,))
    letter = ''
    li = cur.fetchall()
    for i in range(len(li)):
        letter += li[i][0]
    return letter

if __name__ == '__main__':
    con = sqlite3.connect('letters.db')
    letterNum = input('Enter the letter number(or random): ')
    if letterNum == 'random':
        print(retrieveLetter(con, randint(1, 124)))
    else:
        print(retrieveLetter(con, letterNum))
        sectionNumber = input('Enter the section number: ')
        print(retrieveSectionWithNumber(con, letterNum, sectionNumber))
    con.close()