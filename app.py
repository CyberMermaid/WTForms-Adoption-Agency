from flask import Flask, flash, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

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

@app.route("/add", methods=["GET", "POST"])
def AddPetForm():
    """Pet add form; handle adding."""
    form = AddPetForm()
    if form.validate_on_submit():
        # Create a new Pet object with the form data
        new_pet = Pet(name=form.name.data, species=form.species.data, photo_URL=form.photo_URL.data, age=form.age.data, notes=form.notes.data)

        # Add the new pet to the database
        db.session.add(new_pet)
        db.session.commit()

       # Flash a success message and redirect to the homepage
        flash(f"Added {form.species.data} named {form.name.data} of {form.age.data} years old")
        return redirect("/")

    # If the form did not validate, re-render the form with the validation errors
    return render_template(
            "pet_add_form.html", form=form)



connect_db(app)

if __name__ == '__main__':
    app.run(debug=True)

