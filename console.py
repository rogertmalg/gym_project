import pdb

# from models.activity import Activity
# import repositories.activity_repository as activity_repository

# from models.booking import Booking
# import repositories.booking_repository as booking_repository

# from models.instructor import Instructor
# import repositories.instructor_repository as instructor_repository

from models.member import Member
import repositories.member_repository as member_repository

# activity_repository.delete_all()
# booking_repository.delete_all()
# instructor_repository.delete_all()
# member_repository.delete_all()

member_1 = Member("Jess", False, True)
member_repository.save(member_1)


member_1.name = "Jessica"
member_1.premium = True
member_repository.update(member_1)

member_list = member_repository.select_all()
for member in member_list:
    print(member.__dict__)








pdb.set_trace()