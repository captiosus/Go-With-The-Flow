import sqlite3
import csv

conn = sqlite3.connect("login.db")
c = conn.cursor()

def create():
    create = "CREATE TABLE login (user text, pass text)"
    c.execute(create)

def newUser(username, password):

    isTaken = c.execute("SELECT EXISTS(SELECT 1 FROM login WHERE username:uname LIMIT 1)", {"uname":username})
    if (isTaken == 0):
        m = hashlib.sha224(password)
        user = "INSERT INTO login VALUES(username, m.hexdigest())"
        c.execute(user)
        return 1
    else:
        return 0


def authenticate(username, password):
    m = hashlib.sha224(password)
    c = c.execute("SELECT password FROM login WHERE username:uname", {"uname":username})
    if (c == m):
        return 1

    return 0

def calendar(month, firstday, numdays):
    cal = ""
    cal += '<div class="row"> %s </div>'% month

    return cal
