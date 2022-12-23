from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 1) initlize app
app = Flask(__name__)


# 2) tell databse where uri is located, can use mysql etc
# 2) 4 slashes is absolute path, 3 is relative (sqlite:///), database will be in test.db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# initialize database with settings from app
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # returns task __ <- whatever id number it is
    def __repr__(self):
        return '<Task %r>' % self.id


# 1)when you open web page, will display the index html file


@app.get("/")
def index():
    return render_template('index.html')


# 1)
if __name__ == "__main__":
    app.run(debug=False)
