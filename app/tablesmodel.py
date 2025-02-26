from sqlalchemy import Column, String, Integer, TIMESTAMP, text, ForeignKey, Text, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

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

class TourGuide(Base):
    __tablename__ = "tour_guides"
    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String(255), nullable=False)
    cost = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    how_to_go = Column(Text, nullable=False)
    live = Column(Text, nullable=False)
    image_url = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    user = relationship("users", backref="tour_guides")