from db.run_sql import run_sql
from models.member import Member
from models.activity import Activity
from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

def save(activity):
    sql = "INSERT INTO activities (name, instructor_id, room, capacity, date, time, active ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [activity.name, activity.instructor.id, activity.room, activity.capacity, activity.date, activity.time, activity.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity.id = id


def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)
    for result in results:
        instructor = instructor_repository.select(result["instructor_id"])
        activity = Activity(result["name"], instructor, result["room"], result["capacity"], result["date"], result["time"], result["active"], result["id"])
        activities.append(activity)
    return activities


def select(id):
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    instructor = instructor_repository.select(result["instructor_id"])
    activity = Activity(result["name"], instructor, result["room"], result["capacity"], result["date"], result["time"], result["active"], result["id"])
    return activity


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM activities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(activity):
    sql = "UPDATE activities SET (name, instructor_id, room, capacity, date, time, active) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [activity.name, activity.instructor.id, activity.room, activity.capacity, activity.date, activity.time, activity.active, activity.id]
    run_sql(sql, values)


def select_members_in_activity(id):
    attending = []
    sql = "SELECT member.* FROM members INNER JOIN bookings ON bookings.member_id = member.id WHERE bookings.activity_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["name"], result["premium"], result["active"], result["id"])
        attending.append(member)
    return attending