import pdb

from models.activity import Activity
import repositories.activity_repository as activity_repository

# from models.booking import Booking
# import repositories.booking_repository as booking_repository

from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

from models.member import Member
import repositories.member_repository as member_repository

# activity_repository.delete_all()
# booking_repository.delete_all()
# instructor_repository.delete_all()
# member_repository.delete_all()

instructor_1 = Instructor("John", "I like lifiting weights")
instructor_repository.save(instructor_1)
instructor_2 = Instructor("Carla", "I like lifiting weights")
instructor_repository.save(instructor_2)

activity_1 = Activity('Yoga', instructor_1, 'studio 03', 20, '2021-11-25', '11:00', True)
activity_repository.save(activity_1)

activity_1.name = "Hit"
activity_1.instructor = instructor_2
activity_repository.update(activity_1)

# activities = activity_repository.select_all()
# for activity in activities:
#     print(activity.__dict__)

# activity_repository.delete(1)

# print(activity_repository.select(2))

pdb.set_trace()