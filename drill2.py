
import sqlite3

conn = sqlite3.connect('drill.db')



with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT\
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_file) VALUES \
                ('information.docx')"),
    cur.execute("INSERT INTO tbl_files(col_file) VALUES \
                ('hello.txt')"),
    cur.execute("INSERT INTO tbl_files(col_file) VALUES \
                ('myImage.png')"),
    cur.execute("INSERT INTO tbl_files(col_file) VALUES \
                ('myMovie.mpg')"),
    cur.execute("INSERT INTO tbl_files(col_file) VALUES \
                ('world.txt')"),
    cur.execute("INSERT INTO tbl_files(col_file) VALUES \
                ('data.pdf')"),
    cur.execute("INSERT INTO tbl_files(col_file) VALUES \
                ('myPhoto.jpg')")
    conn.commit()
conn.close()


conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file FROM tbl_files WHERE col_file LIKE '%.txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File name: {}".format(item[0])
        print(msg)


