import sqlite3
import csv
import hashlib

#def create():
#    conn = sqlite3.connect("login.db")
#    c = conn.cursor()
#    create = "CREATE TABLE login (user text, pass text)"
#    c.execute(create)

def newUser(username, password):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()
    isTaken = c.execute("SELECT EXISTS(SELECT 1 FROM login WHERE user=:uname LIMIT 1)", {"uname":username})
    if isTaken == 0:
        m = hashlib.sha224(password)
        c.execute("INSERT INTO login VALUES(?, ?)", {username, m.hexdigest()})
        return 1
    return 0


def authenticate(username, password):
    conn = sqlite3.connect("login.db")
    c = conn.cursor()
    m = hashlib.sha224(password)
    c = c.execute("SELECT pass FROM login WHERE user=:uname", {"uname":username})
    if c == m:
        return 1

    return 0

def calendar(month, firstday, numdays):
    cal = ""
    cal += '<div class="row"> %s </div>'% month

    return cal
