from flask import Flask, render_template, request
from sendquery import send_query, get_data

app = Flask(__name__)


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
        sql = "SELECT * FROM `test` WHERE `title` LIKE '%" + title + "%'"

    if sql is None and writer is not None:
        sql = "SELECT * FROM `test` WHERE `writer` LIKE '%" + writer + "%'"
    elif sql is not None and writer is not None:
        sql = sql + "AND `writer` LIKE '%" + writer + "%'"

    if label != 'NULL':
        if sql is None and label is not None:
            sql = "SELECT * FROM `test` WHERE `label` LIKE '%" + label + "%'"
        elif sql is not None and label is not None:
            sql = sql + "AND `label` LIKE '%" + label + "%'"

    if genre != 'NULL':
        if sql is None and genre is not None:
            sql = "SELECT * FROM `test` WHERE `genre` LIKE '%" + genre + "%'"
        elif sql is not None and genre is not None:
            sql = sql + "AND `genre` LIKE '%" + genre + "%'"

    result = get_data(sql)

    return render_template('result.html', result=result[0], count=result[1])


@app.route('/work/<title>', methods=['GET'])
def work(title) -> str:

    sql = "SELECT * FROM `test` WHERE `title` = '" + title + "'"

    result = send_query(sql)

    return render_template('work.html', data=result[0])


@app.route('/writer/<writer>', methods=['GET'])
def writer(writer) -> str:

    sql = "SELECT * FROM `test` WHERE `writer` LIKE '%" + writer + "%'"

    result = get_data(sql)

    return render_template('writer.html', result=result[0], count=result[1], writer=writer)


@app.route('/illust/<illust>', methods=['GET'])
def illust(illust) -> str:

    sql = "SELECT * FROM `test` WHERE `illust` LIKE '%" + illust + "%'"

    result = get_data(sql)

    return render_template('illust.html', result=result[0], count=result[1], illust=illust)


@app.route('/label/<label>', methods=['GET'])
def label(label):

    sql = "SELECT * FROM `test` WHERE `label` LIKE '%" + label + "%'"

    result = get_data(sql)

    return render_template('label.html', result=result[0], count=result[1], label=label)


@app.route('/genre/<genre>', methods=['GET'])
def genre(genre) -> str:

    sql = "SELECT * FROM `test` WHERE `genre` LIKE '%" + genre + "%'"

    result = get_data(sql)

    return render_template('genre.html', result=result[0], count=result[1], genre=genre)


if __name__ == '__main__':
    app.run()
