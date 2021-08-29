import sqlite3
from random import randint

def retrieveSection(con, letterNumber, letterSection):
    #con = sqlite3.connect('letters.db')
    cur = con.cursor()
    cur.execute("SELECT letter_content FROM letters WHERE letter_number=? AND letter_section=?", (letterNumber, letterSection,))
    return cur.fetchall()[0][0]

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
        print(retrieveLetter(con, randint(1, 125)))
    else:
        print(retrieveLetter(con, letterNum))
        sectionNumber = input('Enter the section number: ')
        print(retrieveSection(con, letterNum, sectionNumber))
    con.close()