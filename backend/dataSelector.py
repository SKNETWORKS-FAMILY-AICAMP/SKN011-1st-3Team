import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

user = os.getenv('DB_USER')
host = os.getenv('DB_HOST')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

config = {
    'user':user,
    'password':password,
    'host':host,
    'database':db_name,
    'raise_on_warnings':True,
}

cnx = mysql.connector.connect(**config)


def charge_type_data():
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            cursor.execute("SELECT * FROM CHARGE_TYPE")
            rows = cursor.fetchall()
            resData = {}
            for row in rows:
                resData["수입 여부"] = row[0]
        cnx.close()
        return resData
    else:
        print("Connection Fail")

def brand_data():
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            cursor.execute("SELECT * FROM CHARGE_TYPE")
            rows = cursor.fetchall()
            for row in rows:
                print('수입 여부:',row[0])
        cnx.close()
    else:
        print("Connection Fail")

def db_insert_module(table_name,insert_data):
    for i in insert_data:
        query = f"INSERT INTO {table_name} VALUES {i}"
        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute(query)
                cnx.commit()
        cursor.close()

def charge_info_search(searchItem):
    query = f"SELECT * FROM CHARGE WHERE CHARGE_ADDRESS like '%{searchItem}%'"
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            resData = {}
            for row in rows:
                print(row)
        return resData
    else:
        print("Connection Fail")

charge_info_search('asd')