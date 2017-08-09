import pymysql.cursors  # mySQL Library
import subprocess  # untuk jalanin Exe
import configparser  # config INI file
import yagmail  # Email Library
import arrow  # DateTime Library

#Credential untuk akses mySQLnya
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='barclays',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=False)

with connection.cursor() as cursor:
	sql = """SELECT * from branches limit 10"""
        
        cursor.execute(sql)
        totalrow = cursor.rowcount
        print totalrow
        result = cursor.fetchall()
        for row in result:
        	print row['BranchIdentification']+" "+row['StreetName']

