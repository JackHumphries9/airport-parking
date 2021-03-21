from flask import Flask, request
#from flask_restful import Resource, Api, reqparse
from sqlite3 import *
from json import dumps

app = Flask(__name__)
#api = Api(app)


@app.route('/fetch_data', methods=['GET'])
def get_data():
    db = connect("data.sqlite")
    c = db.cursor()
    c.execute("SELECT col_0, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9 FROM data")

    return str(c.fetchall())


@app.route('/add_data', methods=['GET'])
def add_data():
    if 'row' in request.args and 'col' in request.args and 'content' in request.args:
        try:
            r = request.args['row']
            c = request.args['col']
            t = request.args['content']

            db = connect("data.sqlite")
            dbc = db.cursor()
            dbc.execute('UPDATE data SET col_' + str(c) + ' = "' + t + '" WHERE row_id = ' + str(r))

            db.commit()

            return "true"

        except:
            return "false"
    else:
        return "false"


if __name__ == '__main__':
    app.run(debug=False, port=5000)
