import cx_Oracle
import time
from config import *


def make_connection():
    for _ in range(0, MAX_RETRIES):
        try:
            return cx_Oracle.connect(TNS)
        except Exception as e:
            print(e)
            print('Failed connecting to DB, retrying in 5 seconds')
            time.sleep(5)
    print("Couldn't connect to DB")
    return False


def get_cur(con):
    if con:
        try:
            return con.cursor()
        except Exception as e:
            print(e)
            print("No cursor could be made")
            return False
    else:
        print("No connection, can't continue")
        return False


# todo: make all returns True or False, add actual response message in app.py
def find_latest_id(cur=None):
    # todo: test this thing actually works, or find actual solution in DB settings
    query = """SELECT MAX(ID) from TODO"""
    if cur:
        try:
            return cur.execute(query).fetchall()+1
        except Exception as e:
            print("Whoops, you suck")
            return False
    else:
        print("damn you suck")
        return False


def get_all_todos():
    con = make_connection()
    if con:
        cur = get_cur()
        if cur:
            return (cur.execute(GET_QUERY).fetchall())
        else:
            return "Couldn't make cursor"
    else:
        return "Can't connect to DB :("


def insert_todo(id, string):
    query = INSERT_QUERY.format(int(id), string)
    con = make_connection()
    if con:
        cur = get_cur()
        if cur:
            try:
                cur.execute(query)
                return True
            except Exception as e:
                return "Couldn't insert: " + e
        else:
            return "Couldn't make cursor"
    else:
        return "Can't connect to DB :("


def delete_todo(id):
    query = INSERT_QUERY.format(id)
    con = make_connection()
    if con:
        cur = get_cur()
        if cur:
            try:
                cur.execute(query)
                return True
            except Exception as e:
                return "Couldn't Delete: " + e
        else:
            return "Couldn't make cursor"
    else:
        return "Can't connect to DB :("


global database
database = [{"id": 0, "content": "yeet"}, {"id": 1, "content": "Damn Homie"}]


def get_fakes():
    return database


def insert_fake(task):
    id = len(database)
    database[int(id)] = task
    return "Insertion Successful!"
