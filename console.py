import pdb

# from models.activity import Activity
# import repositories.activity_repository as activity_repository

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

instructor_1.name = "Jessica"
instructor_1.bio = "I like running"
instructor_repository.update(instructor_1)


instructors = instructor_repository.select_all()
for instructor in instructors:
    print(instructor.__dict__)




# 










pdb.set_trace()