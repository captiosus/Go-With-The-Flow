import sqlite3
import csv
import hashlib
import unicodedata
import random
import time

sess = ""
logtime = ""
userstore = ""

def create():
    conn = sqlite3.connect("login.db")
    c = conn.cursor()
    create = "CREATE TABLE login (user text, pass text, userNum text)"
    c.execute(create)

def createPeriod():
    conn = sqlite3.connect("pNum.db")
    c = conn.cursor()
    create = "CREATE TABLE login (usernum text, period integer, cycle integer, pDate integer)"
    c.execute(create)


def newUser(username, password):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()
    isTaken = c.execute("SELECT user FROM login WHERE user=:uname LIMIT 1", {"uname":username})
    data = c.fetchone()
    if data is None :
        m = hashlib.sha224(password)
        u = hashlib.sha224(username)
        query = "INSERT INTO login VALUES (\"%s\", \"%s\", \"%s\")" % (username, m.hexdigest(), u.hexdigest())
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
    print s2
    print m
    if s2 == m:
        userstore = username
        print userstore
        return 1

    return 0

def genToken():
    token = ""
    for x in range(64):
        token += str(random.randrange(0, 9))
    return token

def calendar(month, firstday, numdays):
    cal = ""
    cal += '<div class="row"> %s </div>'% month

    return cal

def enterInfo(period, cycle):
    conn = sqlite3.connect("pNum.db")
    c = conn.cursor()
    u = hashlib.sha224(userstore)
    secs = time.mktime(time.gmtime())
    ins = "INSERT INTO pNum VALUES (\"%s\", %d, %d, %d)" % (u.hexdigest(), period, cycle, secs )
    c.execute(ins)
    conn.commit()

def returnAll(unum):
    u = hashlib.sha224(userstore)
    query = "SELECT usernum FROM pNum WHERE usernum = %s ORDER BY pDate DESC" % (u.hexdigest())
    c.execute(query)
    return c.fetchall()
