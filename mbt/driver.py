from datetime import date

from models import *

generator: Generator = Generator()
alex = SimpleUser(first_name="Alexandros", last_name="Tsakiridis", father_name="Konstantinos")
alex.credentials(username="pacman", password=2460)
alex.birth_date = date(2002, 5, 31)
admin = Administrator(first_name="Grigorios", last_name="Administrator", father_name="Athanassios")
admin.credentials("admin", 1996)
admin.birth_date = date(1996, 2, 24)
nick = Doctor(first_name="Nikolaos", last_name="Palialexis", father_name="Ilias")
nick.credentials(username="oldAlex02", password=1111)
nick.birth_date = date(2002, 4, 26)
for my_user in [SimpleUser.tabs(), alex, admin, nick]: print(my_user)
for my_user in generator.users(10): print(my_user)
