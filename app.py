import json
import sys

import boto3
import psycopg2

from utils.send_push_notification import send_push

# RDS用
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'
DB_USER = 'root'
DB_PASSWORD = 'password'
# s3用
BUCKET_NAME = 'バケット名'
OBJECT_KEY_NAME = 'ファイル名'
s3_client = boto3.client('s3')


def get_connection():
    """ DB接続 """
    return psycopg2.connect(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


def handler(event, context):
    print('start!!')
    # s3からファイルを取得(これはLambdaに権限がいる, IAM)
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY_NAME)
    body = response['Body'].read()
    print(body)

    # rdsと接続しSQL実行
    conn = get_connection()
    cur = conn.cursor()

    # SQL実行（tbl_sampleから全データを取得）
    cur.execute('SELECT * FROM item')  # ここでなぜかエラーがでる
    rows = cur.fetchall()
    print(rows)

    cur.close()
    conn.close()

    print('end!!')
    return 'Hello from AWS Lambda using Python' + sys.version + '!'
