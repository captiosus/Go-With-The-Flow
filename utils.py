import sqlite3
import csv
import hashlib
import unicodedata
import random

sess = ""
logtime = ""
#def create():
#    conn = sqlite3.connect("login.db")
#    c = conn.cursor()
#    create = "CREATE TABLE login (user text, pass text)"
#    c.execute(create)

def newUser(username, password):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()
    isTaken = c.execute("SELECT user FROM login WHERE user=:uname LIMIT 1", {"uname":username})
    data = c.fetchone()
    if data is None :
        m = hashlib.sha224(password)
        query = "INSERT INTO login VALUES (\"%s\", \"%s\")" % (username, m.hexdigest())
        c.execute(query)
        conn.commit()
        return 1
    return 0


def authenticate(username, password):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()
    m = hashlib.sha224(password).hexdigest()
    query = "SELECT pass FROM login WHERE user=\"%s\"" % (username)
    c.execute(query)
    s1 = c.fetchone()
    if s1 == None:
        return 0
    s2 = s1[0]
    if s2 == m:
        print "hello"
        return 1

    return 0

def genToken():
    token = ""
    for x in range(64):
        token += str(random.randrange(0, 9))
    return token
