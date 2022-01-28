import sys

import psycopg2

from utils.send_push_notification import send_push

# psycopg2についての参考(https://chusotsu-program.com/psycopg2-usage/)
# DB接続情報
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'
DB_USER = 'root'
DB_PASSWORD = 'password'

""" psql -h localhost -p 5432 -U postgres """


def get_connection():
    """ DB接続 """
    return psycopg2.connect(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


def handler(event, context):
    print('debug here')
    conn = get_connection()
    cur = conn.cursor()

    # SQL実行（tbl_sampleから全データを取得）
    cur.execute('SELECT * FROM item')
    rows = cur.fetchall()
    print(rows)

    cur.close()
    conn.close()
    print(psycopg2.apilevel)
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
