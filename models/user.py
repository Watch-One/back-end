from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Enum, Integer, String
from config.db import meta, engine

userModel = Table("users", meta,
              Column("id", Integer, primary_key=True),
              Column("name", String(255)),
              Column("email", String(255), unique=True),
              Column("password", String(255)),
              Column("lang", Enum('en', 'es', 'br')))

meta.create_all(engine)