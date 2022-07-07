# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod
import math as mth
import mysql.connector

def uni_split(k):
    counter_comma = 0
    counter_space = 0
    logic = 0
    for i in k:
        if i ==",":
            return k.split(",")
            logic = 1
            break
        if i == "(":
            return k.split("()")
            logic = 1
            break
    if logic == 0:
        return k.split()



def tpl_to_str(a):
    str=""
    for i in a:
        str = str + " " + i
    return str
# Press the green button in the gutter to run the script.
""""
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
"""
def insert_data(data:mysql.connector.connection_cext.CMySQLConnection,nazwa):
    columns = input('Enter your column names with comma {,} eg.( Name,Surname ):')
    dataa = input('Enter data for your columns with space: eg. (data_column1 data_column2) :'.format(columns))
    sql_in_data = dataa.split()
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
        data.cursor().execute(sql_in)
        data.commit()
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
        return name_table
    except:
        print('Unable to create table of data')



if __name__ == '__main__':



    #data = 0
    try:
        data = mysql.connector.connect(host = 'localhost', username = 'root', password = 'Mysql16#',database = "sql-kurs")
        print('Apteka Software')
    except:
        print('Polaczenie nie zostalo nawiazane z baza danych')

    opcja = int(input("Podaj opcje: "))
    z="a b c defg h"
    u="(a bk) (cdef) (ak)"
    while opcja != 0:
        #Configuration
        if opcja == 1:
            #print('z',uni_split(z))
            #print('u:',uni_split(u))
            config_data(data)

            #INSERT , WISE CREATION

        if opcja == 2:
            mycursor = data.cursor()

            mycursor.execute("Show tables;")

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

            nazwa_tab = input('Podaj nazwe tabeli do  ktorj chcesz dane:')
            mycursor.execute("SELECT * FROM {} LIMIT 0".format(nazwa_tab))
            mycursor.fetchall()
            print('W tabeli znajduja sie nastepujace kolumny')
            print(mycursor.description)

            ##Data Insterin"
            insert_data(data,nazwa_tab)

        ## Select
        if opcja == 3:
            ent=input('Enter:')
            if ent == "":
                print("sexy")
            pass


        opcja = int(input("Podaj opcje: "))

"""

    for x in myresult:
        print(x)
    #data.cmd_query()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""