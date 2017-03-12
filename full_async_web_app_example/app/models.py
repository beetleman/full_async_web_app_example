# -*- coding: utf-8 -*-
import peewee
import datetime

from .db import BaseModel


class History(BaseModel):
    user_agent = peewee.TextField(null=False)


class HistoryEntry(BaseModel):
    timestamp = peewee.DateTimeField(default=datetime.datetime.now, null=False)
    history = peewee.ForeignKeyField(History, related_name='entries')
