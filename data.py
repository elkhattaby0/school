import sqlite3

db = sqlite3.connect("data.db")
db.execute("CREATE TABLE IF NOT EXISTS student (Code Text PRIMARY KEY, fname Text, lname Text, date Text, born Text, address Text, email Text, password Text, level Text, grp Text)")
db.execute("CREATE TABLE IF NOT EXISTS worker (Code Text PRIMARY KEY, fname Text, lname Text, date Text, born Text, address Text, email Text, password Text, typeOfWork Text)")

db.execute("CREATE TABLE IF NOT EXISTS math (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")
db.execute("CREATE TABLE IF NOT EXISTS pc (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")

db.execute("CREATE TABLE IF NOT EXISTS svt (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")
db.execute("CREATE TABLE IF NOT EXISTS arabic (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")

db.execute("CREATE TABLE IF NOT EXISTS islamic (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")
db.execute("CREATE TABLE IF NOT EXISTS english (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")

db.execute("CREATE TABLE IF NOT EXISTS french (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")
db.execute("CREATE TABLE IF NOT EXISTS philosophy (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")

db.execute("CREATE TABLE IF NOT EXISTS sport (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")
db.execute("CREATE TABLE IF NOT EXISTS dab (CodeSTD Text PRIMARY KEY, n1 Float, n2 Float, n3 Float, n4 Float, n5 Float)")


# THIS IS FOR ADM

def add_std(code, fname, lname, date, born, address, email, password, level, grp):
   cc = db.cursor()
   cc.execute(f"INSERT INTO student (Code, fname, lname, date, born, address, email, password, level, grp) VALUES('{code}', '{fname}', '{lname}', '{date}', '{born}', '{address}', '{email}', '{password}', '{level}', '{grp}')")
   db.commit()

def edit_std(fname, lname, date, born, address, email, password, level, grp, code):
   cc = db.cursor()
   cc.execute(f"UPDATE student SET fname= '{fname}', lname= '{lname}', date ='{date}', born= '{born}', address= '{address}', email= '{email}', password= '{password}', level= '{level}', grp= '{grp}' WHERE code = '{code}'")
   db.commit()

def delete_std(code):
   cc = db.cursor()
   cc.execute(f"DELETE FROM student WHERE code= '{code}'")
   db.commit()

def display_std(level=0, grp=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM student WHERE level = '{level}'AND grp ='{grp}'")
   return cc.fetchall()

def display_edit(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM student WHERE code = '{code}'")
   return cc.fetchall()

# THIS IS FOR STD

def std_signIn():
   cc = db.cursor()
   cc.execute(f"SELECT * FROM student")
   return cc.fetchall()

def std_Info(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM student WHERE code = '{code}'")
   return cc.fetchall()


# THIS IS FOR WORKER ------------------------------------------

def add_worker(code, fname, lname, date, born, address, email, password, typeOfWork):
   cc = db.cursor()
   cc.execute(f"INSERT INTO worker (Code, fname, lname, date, born, address, email, password, typeOfWork) VALUES('{code}', '{fname}', '{lname}', '{date}', '{born}', '{address}', '{email}', '{password}', '{typeOfWork}')")
   db.commit()

def edit_worker(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM worker WHERE code = '{code}'")
   return cc.fetchall()

def edit_worker1(fname, lname, date, born, address, email, password, typeOfWork, code):
   cc = db.cursor()
   cc.execute(f"UPDATE worker SET fname= '{fname}', lname= '{lname}', date ='{date}', born= '{born}', address= '{address}', email= '{email}', password= '{password}', typeOfWork= '{typeOfWork}' WHERE code = '{code}'")
   db.commit()

def reomve_worker(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM worker WHERE code= '{code}'")
   db.commit()

def display_worker_1():
   cc = db.cursor()
   cc.execute("SELECT * FROM worker")
   return cc.fetchall()
# THIS IS FOR GRADES ------------------------------------------


def add_math(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO math (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_pc(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO pc (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_svt(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO svt (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_arabic(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO arabic (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_islamic(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO islamic (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_english(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO english (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_french(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO french (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_philosophy(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO philosophy (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_sport(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO sport (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

def add_dab(code, n1, n2, n3, n4, n5):
   cc = db.cursor()
   cc.execute(f"INSERT INTO dab (CodeSTD, n1, n2, n3, n4, n5) VALUES('{code}', '{n1}', '{n2}', '{n3}', '{n4}', '{n5}')")
   db.commit()

   #--------- ---
def display_math(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM math WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_math(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE math SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_math(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM math WHERE CodeSTD= '{code}'")
   db.commit()

def display_pc(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM pc WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_pc(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE pc SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_pc(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM pc WHERE CodeSTD= '{code}'")
   db.commit()

def display_svt(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM svt WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_svt(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE svt SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_svt(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM svt WHERE CodeSTD= '{code}'")
   db.commit()

def display_arabic(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM arabic WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_arabic(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE arabic SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_arabic(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM arabic WHERE CodeSTD= '{code}'")
   db.commit()

def display_islamic(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM islamic WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_islamic(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE islamic SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_islamic(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM islamic WHERE CodeSTD= '{code}'")
   db.commit()

def display_english(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM english WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_english(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE english SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_english(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM english WHERE CodeSTD= '{code}'")
   db.commit()

def display_french(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM french WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_french(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE french SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_french(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM french WHERE CodeSTD= '{code}'")
   db.commit()
   
def display_philosophy(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM philosophy WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_philosophy(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE philosophy SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_philosophy(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM philosophy WHERE CodeSTD= '{code}'")
   db.commit()

def display_sport(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM sport WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_sport(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE sport SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_sport(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM sport WHERE CodeSTD= '{code}'")
   db.commit()

def display_dab(code=0):
   cc = db.cursor()
   cc.execute(f"SELECT * FROM dab WHERE CodeSTD = '{code}'")
   return cc.fetchall()
def edit_dab(n1, n2, n3, n4, n5, code):
   cc = db.cursor()
   cc.execute(f"UPDATE dab SET n1= '{n1}', n2= '{n2}', n3 ='{n3}', n4= '{n4}', n5= '{n5}' WHERE CodeSTD = '{code}'")
   db.commit()
def reomve_dab(code=0):
   cc = db.cursor()
   cc.execute(f"DELETE FROM dab WHERE CodeSTD= '{code}'")
   db.commit()


