from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

userModel = Table("groups", meta,
              Column("group_id", String(255)),
              Column("user_id", String(255)))

meta.create_all(engine)