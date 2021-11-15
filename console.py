import pdb

from models.activity import Activity
import repositories.activity_repository as activity_repository

from models.booking import Booking
import repositories.booking_repository as booking_repository

from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

from models.member import Member
import repositories.member_repository as member_repository


booking_repository.delete_all()
activity_repository.delete_all()
instructor_repository.delete_all()
member_repository.delete_all()

member_1 = Member("Bob", False, True)
member_repository.save(member_1)

member_2 = Member("Linda", True, True)
member_repository.save(member_2)

instructor_1 = Instructor("John", True)
instructor_repository.save(instructor_1)

instructor_2 = Instructor("Carla", True)
instructor_repository.save(instructor_2)

activity_1 = Activity('Yoga', instructor_1, 'studio 03', 20, '2021-11-25', '11:00', True)
activity_repository.save(activity_1)

activity_2 = Activity('Hit', instructor_2, 'studio 01', 15, '2021-11-25', '15:00', True)
activity_repository.save(activity_2)

booking_1 = Booking(activity_1, member_1)
booking_repository.save(booking_1)

booking_2 = Booking(activity_1, member_2)
booking_repository.save(booking_2)

attenting_1 = activity_repository.select_members_in_activity(1)
print(len(attenting_1))
for member in attenting_1:
    print(member.__dict__)



# activities = activity_repository.select_all()
# for activity in activities:
#     print(activity.__dict__)

# activity_repository.delete(1)

# print(activity_repository.select(2))

pdb.set_trace()