# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod
import math as mth
import mysql.connector
def tpl_to_str(a):
    str=""
    for i in a:
        str = str + " " + i
    return str
# Press the green button in the gutter to run the script.
def conv_to_parstr(nazwy):
    str_temp = ""

    i = 0

    ilosc = int(len(nazwy)) - 1
    while i <= ilosc:

        if i < ilosc:
            str_temp = str_temp + nazwy[i] + ","
            i = i + 1
        if i == 1:
            str_temp = str_temp + drg[i] + " "
            i = i + 1
    return str_temp

def insert_data(data:mysql.connector.connection_cext.CMySQLConnection,nazwa):
    columns = input('Enter your column names with comma {,} eg.( Name,Surname ):')
    data = input('Enter data for your columns with space: eg. (data_column1 data_column2) :'.format(columns))
    sql_in_data = data.split()
    num = columns.split(',')
    ilosc = int(len(num))
    print(ilosc)
    temp = ["{}"]*ilosc
    temp_t = tuple(temp)
    temp_str = ""
    i=0
    while i < ilosc:
        if i < ilosc-1:
            temp_str = temp_str +"'"+ temp[i]+"'" +","
        if i == ilosc-1:
            temp_str = temp_str +"'"+ temp[i]+"'"
        i=i+1
    temp_sql_in = "INSERT INTO {name} ({str}) VALUES ({mod})".format(name=nazwa, str=columns, mod=temp_str)
    print(temp_sql_in)
    sql_in = temp_sql_in.format(*sql_in_data)

    try:
        print(sql_in)
        #data.cursor().execute(beg)
        #data.commit()
    except:
        print("fail")




def config_data(data:mysql.connector.connection_cext.CMySQLConnection):
    name_table = input('Enter the name of your table:')
    columns = input('Enter your column names with space eg.( Name Surname ):')


    #Data processing
    columns_work = columns.split()
    ilosc = int(len(columns_work)) - 1
    b = ["VARCHAR(255)"] * (ilosc + 1)
    x = tuple(b)
    str = ""
    #Petla przygotowywujaca string
    i = 0

    while i <= ilosc:

        if i < ilosc:
            str = str + " " + columns_work[i] + " " + x[i] + ","
            i = i + 1
        if i == 1:
            str = str +" " + columns_work[i] + " " + x[i]
            i = i + 1

    beg = "CREATE TABLE {name} (id INT AUTO_INCREMENT PRIMARY KEY,".format(name=name_table) + str + ")"
    #Proba utworzenia tabeli
    try:
        data.cursor().execute(beg)
    except:
        print('Unable to create table of data')



if __name__ == '__main__':



    #data = 0
    try:
        data = mysql.connector.connect(host = 'localhost', username = 'root', password = 'Mysql16#',database = "sql-kurs")
        print('Apteka Software')
    except:
        print('Polaczenie nie zostalo nawiazane z baza danych')

    #cur = data.cursor()


    """   STARTER DO PRZEROBKI
        #print(cur.execute("SELECT name FROM users;"))
    try:
        cur.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    except:
        pass
        #SELECT
    """
    z = ["Client1", "Client2"]
    b = ["VARCHAR(255)", "VARCHAR(255)"]
    x = tuple(b)
    drg = tuple(z)
    nazwa = "Awesome"
    opcja = int(input("Podaj opcje: "))
    while opcja != 0:
        #Configuration
        if opcja == 1:

            config_data(data)
            #print(good_config(nazwa,drg))
            #print(type(data))
            #bing = "SELECT {},{} FROM {nazwaa}".format(*drg,nazwaa=nazwa)
            #emk = ["{}"]*3
            #str_tst = tpl_to_str(tuple(emk))
            #ciekawe = "no {}".format(str_tst)
            #print(ciekawe.format(1,2,3))
            #print(bing)
            #cur.execute("SELECT {},{} FROM {nazwaa}".format(nazwaa=nazwa))
            #myresult = cur.fetchall()
            #print(myresult)
            #for x in myresult:
                #print(x)
            #INSERT , WISE CREATION

        if opcja == 2:
                insert_data(data,nazwa)
                """
                #val = len(z)-1
                str = ""

                i=0

                ilosc = int(len(drg))-1
                while i <= ilosc:
                    
                    if i < ilosc:
                        str = str+drg[i]+ " " + x[i] + ","
                        i = i+1
                    if i == 1:
                        str = str + drg[i] + " " + x[i]
                        i= i+1
                #print(str)
                print('Funkcja:',conv_to_parstr(drg))
                beg = "CREATE TABLE {nazwaa} (id INT AUTO_INCREMENT PRIMARY KEY,".format(nazwaa=nazwa)+str+")"
                sql_in = "INSERT INTO {name} ({str}) VALUES ()".format(name=nazwa, str=str)
                #print(beg)
                #print(sql_in)

                #try:
                 #   cur.execute(beg)
                #except:
                 #   print("fail")
        """
        ## INPUTING
        if opcja == 3:
            name = input('Enter name: ')
            postcode = input('Enetr post-code: ')
            val = (name, postcode)
            sql_in = "INSERT INTO {name} ({str}) VALUES ()".format(name=name,str = str)
            #cur.execute(sql_in, val)

            #data.commit()
        opcja = int(input("Podaj opcje: "))

"""

    for x in myresult:
        print(x)
    #data.cmd_query()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""