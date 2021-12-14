from app import db
from posts import User_post

db.drop_all()
db.create_all()
p1 = User_post(title = "Safasf", author = "Egor", description = "Saflamflkanflkankflalfkanlf",
               rendered_data_of_pic = "/home/hacking/PycharmProjects/EPAM_NEW/static/pic/Screenshot from 2021-12-14 16-18-44.png",
               url = '/google.com')
db.session.add(p1)
db.session.commit()

# p1 = User_post(title = "Safasf", author = "Egor", description = "Saflamflkanflkankflalfkanlf")
# db.session.add(p1)
#
# p1 = User_post(title = "Safasf", author = "Egor", description = "Saflamflkanflkankflalfkanlf")
# db.session.add(p1)
#
# p1 = User_post(title = "Safasf", author = "Egor", description = "Saflamflkanflkankflalfkanlf")
# db.session.add(p1)
print("Sfafafk")