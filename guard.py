import sqlite3

def connect():
    con=sqlite3.connect("customers.db")
    c=con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, street TEXT, city_state Text, zip INTEGER, phone INTEGER, sales_rep TEXT, results TEXT, status TEXT, sale_date TEXT, install_date TEXT, lead TEXT)")
    con.commit()
    con.close()

def add(first_name,last_name,street,city_state,zip,phone,sales_rep,results,status,sale_date,install_date,lead):
    con=sqlite3.connect("customers.db")
    c=con.cursor()   
    c.execute("INSERT INTO customer VALUES(Null,?,?,?,?,?,?,?,?,?,?,?,?)",(first_name,last_name,street,city_state,zip,phone,sales_rep,results,status,sale_date,install_date,lead))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("customers.db")
    c=con.cursor()   
    c.execute("SELECT * FROM customer")
    r=c.fetchall()
    con.close()
    return r
    
def search(first_name="",last_name="",street="",city_state="",zip="",phone="",sales_rep="",results="",status="",sale_date="",install_date="",lead=""):
    con=sqlite3.connect("customers.db")
    c=con.cursor()   
    c.execute("SELECT * FROM customer WHERE first_name=? OR last_name=? OR street=? OR city_state=? OR zip=? OR phone=? OR sales_rep=? OR results=? OR status=? OR sale_date=? OR install_date=? Or lead=?",
    (first_name,last_name,street,city_state,zip,phone,sales_rep,results,status,sale_date,install_date,lead))
    r=c.fetchall()
    con.close()
    return r

def delete(id):
    con=sqlite3.connect("customers.db")
    c=con.cursor()   
    c.execute("DELETE FROM customer WHERE id=?",(id,))
    con.commit()
    con.close()

connect()
print(view())
delete(1)
print(view())

