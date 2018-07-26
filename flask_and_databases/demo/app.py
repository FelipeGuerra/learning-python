from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:fodao511@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nnmanietdshycd:1b8081a7095112bd138a62585d9041ff380276016d7006b4a0ce88370652795e@ec2-54-204-21-226.compute-1.amazonaws.com:5432/ddhlh8ccr7bcfe?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])

def success():
    if request.method == "POST":
        email = request.form["email"]
        height = request.form["height"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template('success.html')
            
    return render_template('index.html', html='<div class="alert alert-warning" role="alert">This e-mail already exists!</div>')


if __name__ == '__main__':
    app.debug = True
    app.run()
