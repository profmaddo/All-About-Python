from sqlalchemy import select

from sqlalchemy import Column, create_engine, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, Session

from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "<User(name={0}, fullname={1})>".format(self.name, self.fullname)


class Address(Base):
    __tablename__ = 'user_address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=True)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(email_address='{self.email_address}', user_id='{self.user_id}')"


#print(User.__tablename__)

#print(Address.__tablename__)

engine = create_engine("sqlite:///persona.db")

Base.metadata.create_all(engine)

inpector_engine = inspect(engine)

print(inpector_engine.has_table("user_address"))

print(inpector_engine.get_table_names())

print(inpector_engine.default_schema_name)

with Session(engine) as session:
    maddo = User(
        name="maddo",
        fullname="Marco Oliveira",
    )

    chris = User(
        name="chris",
        fullname="Chris Oliveira",
    )

    session.add_all([maddo, chris])
    session.commit()


stmt = select(User).where(User.name.in_(["maddo", "chris"]))


for user in session.scalars(stmt):
    print(user.name)

