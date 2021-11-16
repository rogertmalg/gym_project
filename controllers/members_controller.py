from flask import Blueprint, Flask, redirect, render_template, request 

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# index
@members_blueprint.route("/members", methods = ["GET"])
def members():
    all_members = member_repository.select_all()
    return render_template("members/index.html", all_members = all_members)

# new - form
@members_blueprint.route("/members/new", methods = ["GET"])
def new_member():
    return render_template("members/new.html")

# create - post 
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    premium = request.form["premium"]
    active = request.form["active"]
    new_member = Member(name, premium, active)
    member_repository.save(new_member)
    return redirect("/members")

# Edit
@members_blueprint.route("/members/<id>/edit", methods = ["GET"])
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

# Update
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    premium = request.form["premium"]
    active = request.form["active"]
    member = Member(name, premium, active, id)
    member_repository.update(member)
    return redirect("/members")

# Delete 
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")