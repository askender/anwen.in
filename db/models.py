# -*- coding:utf-8 -*-

import datetime
from peewee import *
import db_config


if db_config.db['type'] == 'sqlite':
    anwen_db = SqliteDatabase(db_config.db['name'])
elif db_config.db['type'] == 'mysql':
    anwen_db = MySQLDatabase(
        db_config.db['name'],
        user=db_config.db['user'],
        passwd=db_config.db['passwd'])
else:
    info('database error')


class AnwenModel(Model):
    """A base model that will use database"""
    class Meta:
        database = anwen_db


class User(AnwenModel):
    user_name = CharField()
    user_pass = CharField()
    user_email = CharField()
    user_domain = CharField()
    user_url = CharField(default='')
    user_city = CharField(default='')
    user_leaf = IntegerField(default=0)
    user_status = IntegerField(default=0)
    user_say = TextField(default='')
    user_jointime = DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.user_name

    def following(self):
        return User.select().join(
            Relationship, on='to_user_id'
        ).where(from_user=self).order_by('user_name')

    def followers(self):
        return User.select().join(
            Relationship, on='from_user_id'
        ).where(to_user=self).order_by('user_name')

    def is_following(self, user):
        return Relationship.filter(
            from_user=self,
            to_user=user
        ).exists()

    def is_liking(self, share_id):
        return Like.select().filter(
            user_id=self,
            share_id=share_id
        ).exists()


class Ande(AnwenModel):
    user = ForeignKeyField(User)
    usersay = TextField(default='')
    andesay = TextField(default='')
    chattime = DateTimeField(default=datetime.datetime.now)


class Share(AnwenModel):
    user = ForeignKeyField(User)
    title = CharField()
    sharetype = CharField(default='pencil')
    slug = CharField(default='')
    markdown = TextField()
    commentnum = IntegerField(default=0)
    likenum = IntegerField(default=0)
    hitnum = IntegerField(default=0)
    status = IntegerField(default=0)
    published = DateTimeField(default=datetime.datetime.now)
    updated = DateTimeField(default=datetime.datetime.now)


class Comment(AnwenModel):
    user = ForeignKeyField(User)
    share = ForeignKeyField(Share)
    commentbody = TextField()
    commenttime = DateTimeField(default=datetime.datetime.now)


class Like(AnwenModel):
    user = ForeignKeyField(User)
    share = ForeignKeyField(Share)
    liketime = DateTimeField(default=datetime.datetime.now)


class Relationship(AnwenModel):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')

    def __unicode__(self):
        return 'Relationship from %s to %s' % (self.from_user, self.to_user)


class Hit(AnwenModel):
    user = ForeignKeyField(User)
    share = ForeignKeyField(Share)
    hitnum = IntegerField(default=0)
    hittime = DateTimeField(default=datetime.datetime.now)


class Tag(AnwenModel):
    user = ForeignKeyField(User)
    share = ForeignKeyField(Share)
    tagname = TextField()


def main():
    # when you're ready to start querying, remember to connect
    anwen_db.connect()
    User.create_table()
    Ande.create_table()
    Share.create_table()
    Comment.create_table()
    Like.create_table()
    Relationship.create_table()
    Hit.create_table()
    Tag.create_table()
    print('database created')
