from db.run_sql import run_sql
from models.instructor import Instructor

def save(instructor):
    sql = "INSERT INTO instructors (name, bio) VALUES (%s, %s) RETURNING id"
    values = [instructor.name, instructor.bio]
    results = run_sql(sql, values)
    id = results[0]['id']
    instructor.id = id


def select_all():
    instructors = []
    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    for result in results:
        instructor = Instructor(result["name"], result["bio"], result["id"])
        instructors.append(instructor)
    return instructors


def select(id):
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    instructor = Instructor(result["name"], result["bio"], result["id"])
    return instructor


def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM instructors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(instructor):
    sql = "UPDATE instructors SET (name, bio) = (%s, %s) WHERE id = %s"
    values = [instructor.name, instructor.bio, instructor.id]
    run_sql(sql, values)