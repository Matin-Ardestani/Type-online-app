# import sqlite3

# connection = sqlite3.connect('C:/Users/ardes/Desktop/Typing-online-app/src/database.db')
# cursor = connection.cursor()

# quary = "CREATE TABLE acounts (username VARCHAR(100) , email VARCHAR(100), password VARCHAR(100) , ip VARCHAR(100) );"

# cursor.execute("SELECT * FROM acounts;")

# for r in cursor:
#     print(r)


# connection.commit()
# connection.close()

import socket
hostname = socket.getsockname()

print(hostname)