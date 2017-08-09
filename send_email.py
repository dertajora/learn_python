import pymysql.cursors  # mySQL Library
import subprocess  # untuk jalanin Exe
import configparser  # config INI file
import yagmail  # Email Library
import arrow  # DateTime Library
from credential import password_email,variable_import

today = arrow.now().replace(days=0).format("YYYYMMDD")
GMAIL_USER = "cyberindo-product@garena.co.id"
GMAIL_PASS = password_email
TO = ('rakhmand@garena.co.id')
html = ""

html = "Consecutive failed transactions  detected \n So we set OUT OF STOCK <table border=1><tr><td>Name</td><td>Product</td></tr><tr><td>1</td><td>Pulsa XL</td></tr></table>"
content = [html]
HEADER = (today + "_Consecutive Error_Set Out of Stock_" + "AXIS" + " " + "50000")
yag = yagmail.SMTP({GMAIL_USER: "Auto Switch"}, GMAIL_PASS)
yag.send(TO, HEADER, content)

print("Sent email sukses !")
print variable_import