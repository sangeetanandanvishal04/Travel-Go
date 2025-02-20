from passlib.context import CryptContext
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def generate_otp():
    return str(random.randint(1000, 9999))

def send_email(subject: str, recipient_email: str, html_content: str):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = settings.email
    password = settings.smtp_password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(html_content, 'html'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

def send_signup_email(recipient_email: str):
    subject = "Welcome to Speak&Go - Your Ultimate Travel & Language Companion!"
    html_content = """
    <html>
    <body>
        <h2 style="color: #2e6c80;">Welcome to Speak&Go - Your Ultimate Travel & Language Companion!</h2>
        <p>Dear Traveler,</p>
        <p>We're excited to have you onboard! Speak&Go makes your travel smoother and language barriers disappear.</p>
        <p>With Speak&Go, you can:</p>
        <ul>
            <li><strong>Explore destinations in your language:</strong> Get travel guides, landmarks, and transport insights.</li>
            <li><strong>Communicate effortlessly:</strong> Real-time speech translation and text-to-speech synthesis.</li>
            <li><strong>Plan smartly:</strong> Currency conversion, weather updates, and local event recommendations.</li>
            <li><strong>Stay connected anywhere:</strong> Offline mode for travel guides and essential translations.</li>
        </ul>
        <p>Start your journey with Speak&Go today and explore the world like never before!</p>
        <p>Safe travels,<br/>The Speak&Go Team</p>
        <p style="font-size: small; color: gray;">This is a system-generated email. Please do not respond.</p>
    </body>
    </html>
    """
    send_email(subject, recipient_email, html_content)

def send_otp_email(recipient_email: str, otp: str):
    subject = "Your OTP for Secure Access - Speak&Go"
    html_content = f"""
    <html>
    <body>
        <h2 style="color: #2e6c80;">Verify Your Account with OTP</h2>
        <p>Dear User,</p>
        <p>Your One-Time Password (OTP) for secure access to Speak&Go is:</p>
        <h1 style="color: #d9534f;">{otp}</h1>
        <p>Use this OTP to complete your login or password reset request.</p>
        <p>If you didn't request this, please contact our support team immediately.</p>
        <p>Best regards,<br/>The Speak&Go Team</p>
        <p style="font-size: small; color: gray;">This is a system-generated email. Please do not respond.</p>
    </body>
    </html>
    """
    send_email(subject, recipient_email, html_content)  