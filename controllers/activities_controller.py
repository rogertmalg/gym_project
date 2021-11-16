from flask import Blueprint, Flask, redirect, render_template, request 

from models.activity import Activity
import repositories.activity_repository as activity_repository
import repositories.instructor_repository as instructor_repository

activities_blueprint = Blueprint("activities", __name__)

# index
@activities_blueprint.route("/activities", methods = ["GET"])
def activities():
    all_activities = activity_repository.select_all()
    return render_template("activities/index.html", all_activities = all_activities)

# Show 
@activities_blueprint.route("/activities/<id>", methods = ["GET"])
def show_activity(id):
    members = activity_repository.select_members_in_activity(id)
    activity = activity_repository.select(id)
    return render_template("activities/show.html", members=members, activity=activity)

# new - form
@activities_blueprint.route("/activities/new", methods = ["GET"])
def new_activity():
    instructors = instructor_repository.select_all()
    return render_template("activities/new.html", instructors = instructors)

# create - post 
@activities_blueprint.route("/activities", methods=["POST"])
def create_activity():
    name = request.form["name"]
    instructor_id = request.form["instructor_id"]
    instructor = instructor_repository.select(instructor_id)
    room = request.form["room"]
    capacity = request.form["capacity"]
    date = request.form["date"]
    time = request.form["time"]
    active = request.form["active"]
    new_activity = Activity(name, instructor, room, capacity, date, time, active)
    activity_repository.save(new_activity)
    return redirect("/activities")

# Edit
@activities_blueprint.route("/activities/<id>/edit", methods = ["GET"])
def edit_activity(id):
    activity = activity_repository.select(id)
    instructors = instructor_repository.select_all()
    return render_template("activities/edit.html", activity = activity, instructors = instructors)

# Update
@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    name = request.form["name"]
    instructor_id = request.form["instructor_id"]
    instructor = instructor_repository.select(instructor_id)
    room = request.form["room"]
    capacity = request.form["capacity"]
    date = request.form["date"]
    time = request.form["time"]
    active = request.form["active"]
    activity = Activity(name, instructor, room, capacity, date, time, active, id)
    activity_repository.update(activity)
    return redirect("/activities")

# Delete 
@activities_blueprint.route("/activities/<id>/delete", methods=["POST"])
def delete_activity(id):
    activity_repository.delete(id)
    return redirect("/activities")