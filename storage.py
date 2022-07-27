import os
import datetime

from peewee import *

db = PostgresqlDatabase('testdb', user='root', password='root',
                           host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    email = CharField()
    password = CharField()
    verified = IntegerField()
    timestamp = DateTimeField(default=datetime.datetime.now)

db.create_tables([Users])
