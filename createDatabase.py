#!/usr/bin/python3

import sqlite3
import crawler

con = sqlite3.connect('letters.db')
cur = con.cursor()

cur.execute('''CREATE TABLE letters
               (letter_number integer, letter_section integer, letter_content text)''')

for letter_number in range(1, 125):
    letter_section = 0
    while True:
        letter_section += 1
        try:
            cur.execute("INSERT INTO letters VALUES (?, ?, ?)", (letter_number, letter_section, crawler.retrieveSectionBySectionForDatabase(letter_number, letter_section)))
        except:
            break

con.commit()
con.close()