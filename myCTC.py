from os import getenv
from flask import Flask, render_template, request, url_for
import pymssql
import sqlalchemy
import functools

app = Flask(__name__)

# server = getenv("AMETELL-O3040")
# conn = pymssql.connect(server=('AMETELL-O3040'), database='CTC_DATA')
# cursor = conn.cursor()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    server = getenv("AMETELL-O3040")
    conn = pymssql.connect(server=('AMETELL-O3040'), database='CTC_DATA')
    cursor = conn.cursor()
    cursor.execute('SELECT top 10 * FROM Chr_PartHeader where phPartNum like \'%MV4%\'')
    parts = cursor.fetchall()
    # while parts:
    #     print("ID=%d, Name=%s, This=%s" % (row[0], row[1], row[2]))
    #     row = cursor.fetchone()

    cursor.execute('spAddLabel 51523')
    conn.close()

    # parts = 'Hello, through transit.'

    return render_template('this.html', parts=parts)

if __name__ == "__main__":
    app.run()


# server = getenv("AMETELL-O3040")
# conn = pymssql.connect(server=('AMETELL-O3040'), database='CTC_DATA')
# cursor = conn.cursor()
# cursor.execute("""
# IF OBJECT_ID('persons', 'U') IS NOT NULL
#     DROP TABLE persons
# CREATE TABLE persons (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     salesrep VARCHAR(100),
#     PRIMARY KEY(id)
# )
# """)
# cursor.executemany(
#     "INSERT INTO persons VALUES (%d, %s, %s)",
#     [(1, 'John Smith', 'John Doe'),
#      (2, 'Jane Doe', 'Joe Dog'),
#      (3, 'Mike T.', 'Sarah H.')])
# # you must call commit() to persist your data if you don't set autocommit to True
# conn.commit()


# cursor.execute('SELECT top 10 * FROM Chr_PartHeader')
# row = cursor.fetchone()
# while row:
#     print("ID=%d, Name=%s, This=%s" % (row[0], row[1], row[2]))
#     row = cursor.fetchone()
#
# conn.close()
