#Imports

from flask import Flask, redirect, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.helpers import url_for

#Configuration

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:vanarcar08@localhost:5432/carspot"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Models
 
class User(db.Model):
    __tablename__ = "Carros"
    
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(32), nullable=False)
    num = db.Column(db.Integer(), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    plate = db.Column(db.String(6), nullable=False)
    time = db.Column(db.Time(1))

def pay(self):
    total = (time.now-self.time)*0.10


db.create_all()

#Routes

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/revision", methods=["POST"])
def calculate_payment():
    data=request.json
    owner = data["owner"]
    num = data["num"]
    email = data["email"]
    plate = data["plate"]
    time = data["time"]
    

    user = User(
		owner=owner,
		num=num, 
		email=email,
		plate=int(plate),
		time=int(time),
	)

    db.session.add(user)
    db.session.commit()
    payment = user.pay()
    return jsonify({"total_a_pagar": payment}), 200


if __name__ == "__main__":
	app.run(debug=True, port=5000)
    
