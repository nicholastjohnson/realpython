#import sqlite3 and random
import sqlite3
import random

#create connection to sqlite3 database
with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()

    #drop table if it already exists
    c.execute('DROP TABLE if exists numbers')

    #create numbers table for data
    c.execute('CREATE TABLE numbers(num int)')

    #insert 100 random numbers into the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",
                  (random.randint(0,100),))