import mysql.connector as mariadb

sample_db = mariadb.connect(
    host      = "localhost" ,
    user      = "root"      ,
    password  = ""          ,
    database  = "db_name"
)
