import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

# ======== CONFIGURATION SETTINGS ========
SENDER_EMAIL = "Muhammadrebal19@gmail.com"  # Replace with your Gmail
SENDER_PASSWORD = "zmfd cuxc "  # Create app password: https://myaccount.google.com/apppasswords 
RECEIVER_EMAIL = "news@gmail.com"  # Enter recipient email
IMAGE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "1.png")
#IMAGE_FILE = "Desktop/1.jpg"  # Path to your image file
SUBJECT = "Email Testing"
BODY = "THis is test "
# ========================================

def send_email_with_image():
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = SUBJECT

    # Attach body text
    msg.attach(MIMEText(BODY, 'plain'))

    # Attach image
    try:
        with open(IMAGE_FILE, 'rb') as img_file:
            img_data = img_file.read()
        image = MIMEImage(img_data, name=os.path.basename(IMAGE_FILE))
        msg.attach(image)
        print(f"Attached image: {IMAGE_FILE}")
    except FileNotFoundError:
        print(f"Error: Image file not found at {IMAGE_FILE}")
        return False

    # Send email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

if __name__ == "__main__":
    send_email_with_image()