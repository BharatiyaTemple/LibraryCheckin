import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *


#for AWS use this
#DATABASE = MySQLDatabase("checkin", host="AWS KEY.amazonaws.com", port=3306, user="AWS user", passwd="AWS password!")


#to test locally use this
DATABASE = SqliteDatabase('test.db', check_same_thread=False)

class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    @classmethod
    def create_user(cls, email, password, admin=False):
        try:
            with DATABASE.transaction():
                cls.create(
                    email=email,
                    password=generate_password_hash(password),
                    is_admin = admin
                )
        except IntegrityError:
            raise ValueError("User already exists")


class Taco(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    phoneNumber = TextField()
    fullName = TextField()
    email = CharField(unique=True)
    member = TextField(null=True)

    class Meta:
        database = DATABASE


class Check(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    phoneNumber = TextField()

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Taco, Check], safe=True)

    DATABASE.close()