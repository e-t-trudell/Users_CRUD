from flask import Flask, render_template, redirect, request, session
# import the class from model_one.py
from flask_app.models.ucrud import User
app = Flask(__name__)
@app.route("/")
def index():
    # from flask_app.models.model_one import User
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    # users=User.getall()
    return render_template("create.html", users=users)

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["first_name"],
        "lname" : request.form["last_name"],
        "email" : request.form["email"]}
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Redirect after saving to the database.
    return redirect('/displayone')

# displays only one user
@app.route("/displayone")
def displayone():
    users = User.get_one()
    print("Displaying One USER!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(users)
    return render_template("read_one.html", users=User.get_one())

# displays all users
@app.route("/displayall")
def displayall():
    users = User.get_all()
    print("Displaying All USERS!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(users)
    return render_template("read_all.html", users=User.get_all())

# /users/edit/<int:id>
# data = {'id':id}
# render_template(users_edit.html)
# users=User.get_one(data)
@app.route("/edit")
def editme():
    users = User.get_one()
    print(users)
    return render_template("users_edit.html", users=users)

# new  route method must be post method for update user here + redirect to read_one
@app.route('/update_user', methods=["POST"])
def update_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["first_name"],
        "lname" : request.form["last_name"],
        "email" : request.form["email"]}
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Redirect after saving to the database.
    return redirect('/display')

# show redirects to display which renders read_one for user
@app.route("/show")
def show():
    return redirect("/display")

# /users/delete/<int:id>
@app.route("/delete")
def delete():
    User.delete()
    return redirect("read_all.html")