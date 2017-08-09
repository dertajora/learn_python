import pymysql.cursors  # mySQL Library
import subprocess  # untuk jalanin Exe
import configparser  # config INI file
import yagmail  # Email Library
import arrow  # DateTime Library

with open("product.ini", "w") as file:
    file.write("[Product]\n")
    file.write("code = {}\n".format(11122))
    file.write("id = {}\n".format(11))
    file.write("gateway = {}\n".format(111))

print("Write file sukses !")