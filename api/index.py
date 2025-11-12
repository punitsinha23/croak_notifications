from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASSWORD")

#SIGNUP EMAIL



# ---------------------------
# FOLLOW EMAIL
# ---------------------------
class FollowSchema(BaseModel):
    to: EmailStr
    follower_name: str

@app.post("/send-follow-email")
def send_follow_email(data: FollowSchema):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = data.to
        msg["Subject"] = "🎉 New Follower on Crock!"

        plain_text = f"{data.follower_name} started following you on Crock!"

        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
                <div style="max-width:600px; margin:auto; background:white; border-radius:10px; padding:20px;">
                    <h2 style="color:#333;">👋 Hey there!</h2>
                    <p style="font-size:16px; color:#444;">
                        <strong>{data.follower_name}</strong> just started following you on <b>Crock</b>! 🎊
                    </p>
                    <hr style="border:none; border-top:1px solid #eee;">
                    <p style="font-size:14px; color:#777;">
                        Keep sharing awesome content!
                    </p>
                </div>
            </body>
        </html>
        """

        msg.set_content(plain_text)
        msg.add_alternative(html_content, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASS)
            smtp.send_message(msg)

        return {"status": "success", "message": f"Email sent to {data.to}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------
# LIKE EMAIL
# ---------------------------
class LikeSchema(BaseModel):
    to: EmailStr
    username: str

@app.post("/send-like-email")
def send_like_email(data: LikeSchema):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = data.to
        msg["Subject"] = "❤️ Someone Liked Your Post on Crock!"

        plain_text = f"{data.username} liked your post!"

        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
                <div style="max-width:600px; margin:auto; background:white; border-radius:10px; padding:20px;">
                    <h2 style="color:#333;">🔥 Your Post Got Love!</h2>
                    <p style="font-size:16px; color:#444;">
                        <strong>{data.username}</strong> liked your post on <b>Crock</b>! ❤️
                    </p>
                    <a href="https://croak-green-shine.vercel.app/index" style="color:#007BFF; text-decoration:none;">Check it out</a>
                    <hr style="border:none; border-top:1px solid #eee;">
                    <p style="font-size:14px; color:#777;">
                        Keep posting great stuff!
                    </p>
                </div>
            </body>
        </html>
        """

        msg.set_content(plain_text)
        msg.add_alternative(html_content, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASS)
            smtp.send_message(msg)

        return {"status": "success", "message": f"Email sent to {data.to}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------
# SEND OTP EMAIL
# ---------------------------
class OtpSchema(BaseModel):
    to: EmailStr
    otp: str

@app.post("/send-otp-email")
def send_otp_email(data: OtpSchema):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = data.to
        msg["Subject"] = "🔐 Your OTP Code for Verification"

        plain_text = f"Your OTP code is: {data.otp}"

        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
                <div style="max-width:600px; margin:auto; background:white; border-radius:10px; padding:20px;">
                    <h2 style="color:#333;">Verify Your Email</h2>
                    <p style="font-size:16px; color:#444;">
                        Your One-Time Password (OTP) is:
                    </p>
                    <h1 style="color:#007BFF; text-align:center;">{data.otp}</h1>
                    <p style="font-size:14px; color:#777;">
                        This code will expire in 5 minutes. Please do not share it with anyone.
                    </p>
                </div>
            </body>
        </html>
        """

        msg.set_content(plain_text)
        msg.add_alternative(html_content, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASS)
            smtp.send_message(msg)

        return {"status": "success", "message": f"OTP sent to {data.to}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send OTP: {e}")
    
class signUpSchema(BaseModel):
    to: EmailStr
    username: str

@app.post("/send-signup-email")
def send_signup_email(data: signUpSchema):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = data.to
        msg["Subject"] = "Welcome to Crock! 🎉"

        plain_text = f"Hi {data.username}, welcome to Crock!"

        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
                <div style="max-width:600px; margin:auto; background:white; border-radius:10px; padding:20px;">
                    <h2 style="color:#333;">Welcome Aboard, {data.username}!</h2>
                    <p style="font-size:16px; color:#444;">
                        We're thrilled to have you join the Crock community! 🚀
                    </p>
                    <hr style="border:none; border-top:1px solid #eee;">
                    <p style="font-size:14px; color:#777;">
                        Start exploring and sharing your moments with us!
                    </p>
                </div>
            </body>
        </html>
        """

        msg.set_content(plain_text)
        msg.add_alternative(html_content, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASS)
            smtp.send_message(msg)

        return {"status": "success", "message": f"Welcome email sent to {data.to}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class commentSchema(BaseModel):
    to: EmailStr
    username: str
    comment: str

@app.post("/send-comment-email")
def send_comment_email(data: commentSchema):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL 
        msg["To"] = data.to
        msg["Subject"] = "💬 New Comment on Your Post!"
        plain_text = f"{data.username} commented: {data.comment}"
        html_content = f"""        <html>
            <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
                <div style="max-width:600px; margin:auto; background:white; border-radius:10px; padding:20px;">
                    <h2 style="color:#333;">New Comment Alert!</h2>
                    <p style="font-size:16px; color:#444;">
                        <strong>{data.username}</strong> commented on your post:
                    </p>
                    <blockquote style="font-size:14px; color:#555; border-left:4px solid #eee; margin:10px 0; padding-left:10px;">
                        {data.comment}
                    </blockquote>
                    <hr style="border:none; border-top:1px solid #eee;">
                    <p style="font-size:14px; color:#777;">
                        Engage with your audience and keep the conversation going!
                    </p>
                </div>
            </body>
            </html>"""
        msg.set_content(plain_text)
        msg.add_alternative(html_content, subtype="html")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL, PASS)
            smtp.send_message(msg)
        return {"status": "success", "message": f"Comment notification sent to {data.to}"}
    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))

handler = Mangum(app)