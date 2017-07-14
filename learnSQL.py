import sqlite3
conn=sqlite3.connect('MyDatabase.db')
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE LearnPython1(Language VARCHAR, Version REAL, Skill TEXT)")
    #create_table()

def enter_data():
    c.execute("INSERT INTO LearnPython1 VALUES('Python',2.7,'Beginner')")
    c.execute("INSERT INTO LearnPython1 VALUES('Python',3.5,'Intermediate')")
    c.execute("INSERT INTO LearnPython1 VALUES('Python',3.6,'Expert')")
    conn.commit()

def enter_dynamic_data():
    lang=input("What language? ")
    version=input("What version? ")
    skill=input("What skill level? ")
    c.execute("INSERT INTO LearnPython1(Language, Version, Skill) VALUES(?,?,?)",(lang,version,skill))
    conn.commit()

def read_table_data():
    sql="SELECT * FROM LearnPython1"
    for row in c.execute(sql):
        print(row)
    whatSkill=input("What skill you are looking for? ")
    whatLanguage=input("What language you are looking for? ")
    whatVersion=input("What version do you want to update? ")
    sql="UPDATE LearnPython1 SET Version=? where Version=?"
    newVersion=input("New Version value: ")
    c.execute(sql,[(newVersion),(whatVersion)])
    sql="SELECT * FROM LearnPython1 WHERE Skill==? AND Language==?"
    for row in c.execute(sql,[(whatSkill),(whatLanguage)]):
        print(row)
        #print(row[0])
    conn.commit()
    
#create_table()
#enter_data()
#enter_dynamic_data()
read_table_data()              
conn.close()
    
