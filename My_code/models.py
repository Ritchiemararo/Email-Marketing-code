from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from database import Base

class user(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    org_id = Column(Integer, ForeignKey('organization.id'))
    date_created = Column(DateTime, default=func.now())

    organization = relationship("organization", back_populates="user")
    outbox = relationship("outbox", back_populates="user")

class outbox(Base):
    __tablename__ = "outbox"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    template_id = Column(Integer, ForeignKey('template.id'))
    emailaddress_id = Column(Integer, ForeignKey('emailaddress.id'))
    org_id = Column(Integer, ForeignKey('organization.id'))
    status_id= Column(Integer, ForeignKey('status.id'))

    user = relationship("user", back_populates="outbox")
    template = relationship("template", back_populates="outbox")
    emailaddress = relationship("emailaddress", back_populates="outbox")
    organization = relationship("organization", back_populates="outbox")
    status= relationship("status", back_populates="outbox")

class organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    date_created = Column(DateTime, default=func.now())

    user = relationship("user", back_populates="organization")
    outbox = relationship("outbox", back_populates="organization")

class template(Base):
    __tablename__ = "template"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime, default=func.now())
    data = Column(String, index=True)

    outbox = relationship("outbox", back_populates="template")

class emailaddress(Base):
    __tablename__ = "emailaddress"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    date_created = Column(DateTime, default=func.now())

    outbox = relationship("outbox", back_populates="emailaddress")

class status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True)

    outbox = relationship("outbox", back_populates="status")

class subscriber(Base):
    __tablename__ = "subscriber"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_created = Column(DateTime, default=func.now())
    email = Column(String, index=True)
