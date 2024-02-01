from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
# this line tells the application that we're using postgresql on a local host -> (:///)
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    firts_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)



# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
ada_lovelace = Programmer(
    firts_name ="Ada",
    last_name ="Lovelace",
    gender ="F",
    nationality ="British",
    famous_for ="First Programmer"
)

alan_turing = Programmer(
    firts_name ="Alan",
    last_name ="Turing",
    gender ="M",
    nationality ="British",
    famous_for ="Modern Computing"
)

grace_hopper = Programmer(
    firts_name ="Grace",
    last_name ="Hopper",
    gender ="F",
    nationality ="American",
    famous_for ="COBOL language"
)

margaret_hamilton = Programmer(
    firts_name ="Margaret",
    last_name ="Hamilton",
    gender ="F",
    nationality ="American",
    famous_for ="Apollo 11"
)

bill_gates = Programmer(
    firts_name ="Bill",
    last_name ="Gates",
    gender ="M",
    nationality ="American",
    famous_for ="Microsoft"
)

tim_berners_lee = Programmer(
    firts_name ="Tim",
    last_name ="Berners-Lee",
    gender ="M",
    nationality ="British",
    famous_for ="World Wide Web"
)

istvan_vizhanyo = Programmer(
    firts_name ="Istvan",
    last_name ="Vizhanyo",
    gender = "M",
    nationality ="Hungarian",
    famous_for ="Code Institute Student"
)

# add each instance of the Programmer class to the session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(istvan_vizhanyo)

# commit our session to the database
# session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# commit our session to the database
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#    if person.gender == "F":
#        person.gender = "Female"
#    elif person.gender == "M":
#        person.gender = "Male"
#    else:
#        print("Gender not defined")
#    session.commit()


# deleting a single record
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(firts_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.firts_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")



# query the database for all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id,
          programmer.firts_name + " " + programmer.last_name,
          programmer.gender,
          programmer.nationality,
          programmer.famous_for,
          sep=" | "
    )