import mysql.connector as mysql

host = "localhost"
user = 'root'
password = 'qwerty123'

def main():
    global sql_create
    print('working on mysql')
    db = None
    cur = None
    try:
        db = mysql.connect(host=host,user=user, password=password, database = 'world')
        cur = db.cursor(prepared=True)
        cur.execute(
            "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
        cur.executemany(sql, val)
        db.commit()
        print("done")
    except mysql.errors as err:
        print("Error")
    try:
        cur.execute("SELECT name, address FROM customers")
        myresult = cur.fetchall()
        for i in myresult:
            print(i)
    except mysql.errors as err:
        print("something went wrong")


if __name__ == '__main__':
    main()