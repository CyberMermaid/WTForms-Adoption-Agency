from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Testing'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
debug.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


@app.route("/")
def list_pets():
    """List pets"""
    pets = Pet.query.all()
    return render_template("list.html", pets=pets) 



connect_db(app)

if __name__ == '__main__':
    app.run(debug=True)

