from flask import Blueprint, Flask, redirect, render_template, request 

from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

instructors_blueprint = Blueprint("instructors", __name__)

# index
@instructors_blueprint.route("/instructors")
def instructors():
    all_instructors = instructor_repository.select_all()
    return render_template("instructors/index.html", all_instructors = all_instructors)

# new - form
@instructors_blueprint.route("/instructors/new")
def new_instructor():
    return render_template("instructors/new.html")

# create - post 
@instructors_blueprint.route("/instructors", methods=["POST"])
def create_instructor():
    name = request.form["name"]
    active = request.form["active"]
    new_instructor = Instructor(name, active)
    instructor_repository.save(new_instructor)
    return redirect("/instructors")

# Edit
@instructors_blueprint.route("/instructors/<id>/edit")
def edit_instructor(id):
    instructor = instructor_repository.select(id)
    return render_template("instructors/edit.html", instructor = instructor)

# Update
@instructors_blueprint.route("/instructors/<id>", methods=["POST"])
def update_instructor(id):
    name = request.form["name"]
    active = request.form["active"]
    instructor = Instructor(name, active)
    instructor_repository.update(instructor)

# Delete 
@instructors_blueprint.route("/instructors/<id>/delete", methods=["POST"])
def delete_instructor(id):
    instructor_repository.delete(id)
    return redirect("/instructors")