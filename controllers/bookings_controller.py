from flask import Blueprint, Flask, redirect, render_template, request 

from models.booking import Booking
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

# index
@bookings_blueprint.route("/bookings")
def bookings():
    all_bookings = booking_repository.select_all()
    return render_template("bookings/index.html", all_bookings = all_bookings)


# new - form
@bookings_blueprint.route("/bookings/new")
def new_booking():
    activities = activity_repository.select_all()
    members = member_repository.select_all()
    return render_template("bookings/new.html", activities = activities, members = members)

# create - post 
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_activity():
    activity_id = request.form["activity_id"]
    member_id = request.form["member_id"]
    activity = activity_repository.select(activity_id)
    member = member_repository.select(member_id)
    new_booking = Booking(activity, member)
    booking_repository.save(new_booking)
    return redirect("/bookings")

# Edit
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    activities = activity_repository.select_all()
    members = member_repository.select_all()
    return render_template("bookings/edit.html", booking = booking, activities = activities, members = members)

# Update
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    activity_id = request.form["activity_id"]
    member_id = request.form["member_id"]
    activity = activity_repository.select(activity_id)
    member = member_repository.select(member_id)
    booking = Booking(activity, member, id)
    booking_repository.update(booking)
    return redirect("/bookings")

# Delete 
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")