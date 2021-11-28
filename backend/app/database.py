from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:abcdef12@shrine_mysql:3306/Student"
# tableName='student_info'

engine = create_engine(SQLALCHEMY_DATABASE_URL,)
# #if not engine.dialect.has_table(engine, tableName):  # If table don't exist, Create.
# if inspect(engine).has_table(tableName, 'Student'):
#     metadata = MetaData(engine)
#     # Create a table with the appropriate Columns
#     Table(tableName, metadata,
#           Column('std_id', Integer, primary_key=True, autoincrement=True), 
#           Column('std_name', String(32)),
#           Column('course_name', String(32)),
#           Column('batch', String(32)),
#           Column('tch_name', String(32)),
#           Column('fees', Integer))
#     # Implement the creation
#     metadata.create_all()

SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)

Base = declarative_base()
