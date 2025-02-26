from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    phone_number: str
    country: str
    state: str
    city: str

class UserOut(BaseModel):
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True 

class UserLogin(BaseModel):
    email: EmailStr
    password: str     

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None 

class PasswordChange(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str

class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str
    confirm_password: str   

class OTP(BaseModel):
    email: EmailStr
    otp: str 

class TourGuideCreate(BaseModel):
    destination: str
    cost: int
    description: str
    how_to_go: str
    live: str
    image_url: Optional[str] = None

class TourGuideOut(TourGuideCreate):
    id: int
    class Config:
        from_attributes = True    