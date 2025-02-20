from fastapi import FastAPI, status, HTTPException, Depends, BackgroundTasks
from .database import get_db, engine
from sqlalchemy.orm import Session
from . import schemas, tablesmodel, utils, oAuth2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#origins = ["www.youtube.com", "www.google.com"]
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tablesmodel.Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message" : "Welcome to my API...."}

""" {
    "full_name": "Vishal Singh",
    "email": "email@iiita.ac.in",
    "password": "password",
    "phone_number": "9876543210",
    "country": "India",
    "state": "Uttar Pradesh",
    "city": "Gorakhpur"
} """
@app.post("/signup", response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user_found = db.query(tablesmodel.User).filter(tablesmodel.User.email == user.email).first()

    if user_found:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Email already exists")

    hashed_password = utils.hash(user.password)
    
    new_user = tablesmodel.User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        phone_number=user.phone_number,
        country=user.country,
        state=user.state,
        city=user.city
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    background_tasks.add_task(utils.send_signup_email, user.email)
    return new_user

""" {
    "email": "email@iiita.ac.in",
    "password": "password"
} """
@app.post("/login")
async def login_user(user_credentials:schemas.UserLogin ,db: Session = Depends(get_db)):

    user = db.query(tablesmodel.User).filter(tablesmodel.User.email==user_credentials.email).first()

    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    access_token = oAuth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "Bearer"}

#http://127.0.0.1:8000/forgot-password/email@iiita.ac.in
@app.post("/forgot-password/{email}")
async def forgot_password(email: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user = db.query(tablesmodel.User).filter(tablesmodel.User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with this email does not exist")

    otp = utils.generate_otp()
    db_otp = tablesmodel.OTP(email=email, otp=otp)
    db.add(db_otp)
    db.commit()
    background_tasks.add_task(utils.send_otp_email, user.email, otp)

    return {"message": "OTP sent successfully"}             