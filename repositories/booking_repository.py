from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
import repositories.member_repository as member_repository
from models.activity import Activity
import repositories.activity_repository as activity_repository

def save(booking):
    sql = "INSERT INTO bookings (activity_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [booking.activity.id, booking.member.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        activity = activity_repository.select(result["activity_id"])
        member = member_repository.select(result["member_id"])
        booking = Booking(activity, member, result["id"])
        bookings.append(booking)
    return bookings


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    activity = activity_repository.select(result["activity_id"])
    member = member_repository.select(result["member_id"])
    booking = Booking(activity, member, result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE bookings SET (activity_id, member_id) = (%s, %s) WHERE id = %s"
    values = [booking.activity.id, booking.member.id, booking.id]
    run_sql(sql, values)