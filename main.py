# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod
import math as mth
import mysql.connector

# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    #data = 0
    try:
        data = mysql.connector.connect(host = 'localhost', username = 'root', password = 'Mysql16#',database = "sql-kurs")
        print('Apteka Software')
    except:
        print('Polaczenie nie zostalo nawiazane z baza danych')

    cur = data.cursor()
        #print(cur.execute("SELECT name FROM users;"))
    try:
        cur.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    except:
        pass
        #SELECT


    opcja = int(input("Podaj opcje: "))
    while opcja != 0:
        if opcja == 1:
            cur.execute("SELECT * FROM customers")
            myresult = cur.fetchall()
            print(myresult)
            #for x in myresult:
                #print(x)
            #INSERT
        if opcja == 2:
                pass
        if opcja == 3:
            name = input('Enter name: ')
            postcode = input('Enetr post-code: ')
            val = (name, postcode)
            sql_in = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            cur.execute(sql_in, val)

            data.commit()
        opcja = int(input("Podaj opcje: "))

"""

    for x in myresult:
        print(x)
    #data.cmd_query()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""