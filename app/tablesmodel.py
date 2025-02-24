from sqlalchemy import Column, String, Integer, TIMESTAMP, text, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    country = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class OTP(Base):
    __tablename__ = 'otps'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, ForeignKey('users.email'))
    otp = Column(String, nullable=False)     