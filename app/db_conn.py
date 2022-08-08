import MySQLdb

sql_server_string = "localhost"
username = "root"
password = "test1234"

db = MySQLdb.connect(sql_server_string, username, password)
