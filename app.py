from flask import Flask, render_template
import datetime
from controllers.instructors_controller import instructors_blueprint
from controllers.members_controller import members_blueprint
from controllers.activities_controller import activities_blueprint
from controllers.bookings_controller import bookings_blueprint
import repositories.activity_repository as activity_repository

app = Flask(__name__)

app.register_blueprint(instructors_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def main():
    activities = activity_repository.select_all()
    return render_template('index.html', activities = activities, datetime=datetime)

if __name__ == '__main__':
    app.run()