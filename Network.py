#Wyatt Humnphreys CNA 330 9/20/18
#Sources: https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
#https://www.periscopedata.com/blog/python-create-table
#https://realpython.com/python-csv/

import os, sqlite3

con = sqlite3.connect("network.db")
cur = con.cursor()
cur.execute('''CREATE TABLE hosts (id INTEGER PRIMARY KEY, hostname TEXT, url TEXT, ip TEXT, localremote TEXT, description TEXT);''') # use your column names here


cur.execute('''INSERT INTO hosts VALUES (1, 'Google', 'www.google.com', '8.8.8.8', 'remote', 'Googles DNS Address');''')
cur.execute('''INSERT INTO hosts VALUES (2, 'Renton Technical College', 'www.rtc.edu', '192.124.249.10', 'remote', 'Renton Technical Website');''')
cur.execute('''INSERT INTO hosts VALUES (3, 'Microsoft', 'www.microsoft.com', '191.239.213.197', 'remote', 'Microsofts Website');''')
cur.execute('''INSERT INTO hosts VALUES (4, 'My-PC', 'Wyatt-Desktop', '127.0.0.1', 'local', 'My Computer');''')
cur.execute('''INSERT INTO hosts VALUES (5, 'My Router', 'LinuxRTR', '192.168.0.1', 'local', 'My Router');''')
cur.execute('''INSERT INTO hosts VALUES (6, 'My Printer', 'LocalPrinter', '192.168.0.55', 'local', 'My Printer');''')
con.commit()


print("Remote Hosts: ")
remotegrabber = cur.execute('''SELECT * FROM hosts WHERE localremote == 'remote';''')
for i in remotegrabber:
    print(i)

print(" ")

localgrabber = cur.execute('''SELECT * FROM hosts WHERE localremote == 'local';''')
print("Local Hosts: ")
for i in localgrabber:
    print(i)
con.close()

