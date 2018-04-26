from flask import Flask, render_template, request
import pymysql
import json

app = Flask(__name__)


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


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/search')
def search() -> str:
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def post_search() -> str:

    title = request.form['title']
    label = request.form['label']
    writer = request.form['writer']
    genre = request.form['genre']

    if title is not None:
        sql = "SELECT * FROM `test` WHERE `title` LIKE '%{0}%'".format(title)

    if sql is None and writer is not None:
        sql = "SELECT * FROM `test` WHERE `writer` LIKE '%{0}%'".format(writer)
    elif sql is not None and writer is not None:
        sql = sql + "AND `writer` LIKE '%{0}%'".format(writer)

    if label != 'NULL':
        if sql is None and label is not None:
            sql = "SELECT * FROM `test` WHERE `label` LIKE '%{0}%'".format(label)
        elif sql is not None and label is not None:
            sql = sql + "AND `label` LIKE '%{0}%'".format(label)

    if genre != 'NULL':
        if sql is None and genre is not None:
            sql = "SELECT * FROM `test` WHERE `genre` LIKE '%{0}%'".format(genre)
        elif sql is not None and genre is not None:
            sql = sql + "AND `genre` LIKE '%{0}%'".format(genre)

    result = get_data(sql)

    return render_template('result.html', result=result[0], count=result[1])


@app.route('/work/<title>', methods=['GET'])
def work(title) -> str:

    sql = "SELECT * FROM `test` WHERE `title` = {0}".format(title)

    result = send_query(sql)

    return render_template('work.html', data=result[0])


@app.route('/writer/<writer>', methods=['GET'])
def writer(writer) -> str:

    sql = "SELECT * FROM `test` WHERE `writer` = {0}".format(writer)

    result = get_data(sql)

    return render_template('writer.html', result=result[0], count=result[1], writer=writer)


@app.route('/illust/<illust>', methods=['GET'])
def illust(illust) -> str:

    sql = "SELECT * FROM `test` WHERE `illust` = {0}".format(illust)

    result = get_data(sql)

    return render_template('illust.html', result=result[0], count=result[1], illust=illust)


@app.route('/label/<label>', methods=['GET'])
def label(label):

    sql = "SELECT * FROM `test` WHERE `label` = {0}".format(label)

    result = get_data(sql)

    return render_template('label.html', result=result[0], count=result[1], label=label)


@app.route('/genre/<genre>', methods=['GET'])
def genre(genre) -> str:

    sql = "SELECT * FROM `test` WHERE `genre` = {0}".format(genre)

    result = get_data(sql)

    return render_template('genre.html', result=result[0], count=result[1], genre=genre)


if __name__ == '__main__':
    app.run()
