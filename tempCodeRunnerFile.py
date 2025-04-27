c.execute("DELETE from clients WHERE rowid=1")
print(c.fetchall())