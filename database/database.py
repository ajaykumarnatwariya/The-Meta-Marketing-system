from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.reflection import Inspector

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/database001"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_all_tables():
    Base.metadata.create_all(bind=engine)
