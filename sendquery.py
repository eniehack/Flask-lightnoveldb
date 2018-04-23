import pymysql
import json


def send_query(sql):

    with open('sql.json', 'r') as f:
        data = json.load(f)
        connector = pymysql.connect(
            host=data['host'],
            db=data['db'],
            user=data['user'],
            passwd=data['pass'],
            charset=data['charset']
        )

    with connector.cursor() as cursor:
        cursor.execute(sql)
        get_query = cursor.fetchall()

    return get_query


def get_data(sql):
    get_query = send_query(sql)

    data = []
    result = []
    count = 0

    for row in get_query:
        data.append(row[0])
        count = count + 1

    result.append(data)
    result.append(count)

    return result
