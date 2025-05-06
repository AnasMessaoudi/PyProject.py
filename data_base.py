import sqlite3
#create table
conn= sqlite3.connect('client_data.db')
c = conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS clients(
        bank TEXT  ,
        name TEXT  ,
        age INTEGER,
        salary INTEGER,
        password TEXT,
        loan INTEGER,
        duration REAL,
        current_money INTEGER
          )   ''') 
c.execute("DELETE from clients WHERE rowid=2")
conn.commit()
conn.close()
#print all
def show_clients():
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT rowid, * FROM clients")
  items=c.fetchall()
  for item in items:
    print(item)
  conn.close()
def add_client_to_db(bank,name,age,salary,password,loan,duration,current_money):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("INSERT INTO clients VALUES (?,?,?,?,?,?,?,?)",(bank,name,age,salary,password,loan,duration,current_money))
  new_id = c.lastrowid
  conn.commit()
  conn.close()
  return new_id
#check password for sign in
def check_pw(id,pw):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT password from clients where rowid=?", (id,))
  result = c.fetchone()
  correct=True
  if pw!=result[0]:#result ya5dh el case elli ba3d el password 
    correct=False
  conn.close()
  return correct
#updating client money after withdraw 
def update_client_current_money(id,amount):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("UPDATE clients SET current_money=?  WHERE rowid=?", (amount,id))
  conn.commit()
  conn.close()
#check if id exists in db 
def check_existance(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT 1 FROM clients WHERE rowid = ?", (id,))
  res=c.fetchone()
  c.close()
  return res
def get_salary(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT salary from clients where rowid=?", (id,))
  res=c.fetchone()[0]
  conn.close()
  return res
def get_age(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT age from clients where rowid=?", (id,))
  res=c.fetchone()[0]
  conn.close()
  return res
def get_name(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT name from clients where rowid=?", (id,))
  res=c.fetchone()[0]
  conn.close()
  return res
def get_bank(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT bank from clients where rowid=?", (id,))
  res=c.fetchone()[0]
  conn.close()
  return res
def get_loan(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT loan from clients where rowid=?", (id,))
  res=c.fetchone()[0]
  conn.close()
  return res
def get_duration(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT duration from clients where rowid=?", (id,))
  res=c.fetchone()[0]
  conn.close()
  return res
def get_current_money(id):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("SELECT current_money from clients where rowid=?", (id,))
  res=c.fetchone()[0]
  conn.close()
  return res
def update_client_bank(id,l):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("UPDATE clients SET bank=?  WHERE rowid=?",(l, id))
  conn.commit()
  conn.close()
def update_client_loan(id,l):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("UPDATE clients SET loan=?  WHERE rowid=?",(l, id))
  conn.commit()
  conn.close()
def update_client_salary(id,l):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("UPDATE clients SET salary=?  WHERE rowid=?", (l, id))
  conn.commit()
  conn.close()
def update_client_duration(id,l):
  conn= sqlite3.connect('client_data.db')
  c = conn.cursor()
  c.execute("UPDATE clients SET duration=? WHERE rowid=?", (l, id))
  conn.commit()
  conn.close()
