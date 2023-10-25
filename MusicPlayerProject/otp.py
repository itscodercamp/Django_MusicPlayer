import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate("MusicPlayerProject/adminsdk.json")
firebase_admin.initialize_app(cred)

# Function to send OTP to a phone number
def send_otp(phone_number):
    try:
        user = auth.create_user(phone_number=phone_number)
        return user.uid
    except Exception as e:
        return str(e)

# Function to verify OTP
def verify_otp(uid, otp):
    try:
        auth.verify_phone_number(uid, otp)
        return True
    except auth.PhoneNumberVerificationError:
        return False
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Example: Send OTP to a phone number
    phone_number = input('enter your Number with country code ex: +91 -->  ')
    user_uid = send_otp(phone_number)
    print(f"OTP sent to {phone_number}. User UID: {user_uid}")

    # Example: Verify OTP
    entered_otp = input("Enter the OTP: ")
    if verify_otp(user_uid, entered_otp):
        print("OTP verified successfully!")
    else:
        print("Invalid OTP. Please try again.")
