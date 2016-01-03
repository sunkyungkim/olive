import sqlite3

if __name__ == "__main__" :
  conn = sqlite3.connect('oliverep')
  
  c = conn.cursor()
  
#  c.execute("create table t_test1 (query text)")
  c.execute("insert into t_test1 values ('select * from dual')")
  
  conn.commit()
  
  conn.close()