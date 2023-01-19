import os

from flask import Flask, g
import sqlite3

app = Flask(__name__)
DATABASE = './employees.db'


def make_dicts(cursor, row):
    """
    This function is used by get_db to configure the row factory. Consquently, connections established with
    get_db() will return dictionary objects by default.
    :return: Dict of rows
    """
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    """
    This function configures the database connection.
    :return: Flask sqlite3 database connection object
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db


@app.teardown_appcontext
def close_connection(exception):
    """This function closes the database connection on teardown."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/employees", methods=["GET"])
def employees():
    """
    This function returns a dictionary of all employee records.
    :return: Dict of all employee records
    """
    cur = get_db().cursor()
    sql = "SELECT * FROM employees;"
    records = cur.execute(sql).fetchall()

    return records


if __name__ == "__main__":
    if "PORT" in os.environ and os.environ["PORT"].isdigit() and 1024 < int(os.environ["PORT"]) < 49151:
        port = os.environ["PORT"]
    else:
        print("No valid port set. Port must be castable as an integer and between 1024 and 49151.")
        port = 5050
    app.run(port=port)
